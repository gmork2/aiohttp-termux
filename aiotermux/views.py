import json
import logging
from typing import Callable

from aiohttp.web_exceptions import HTTPMethodNotAllowed, HTTPBadRequest
from aiohttp.web import Request
from aiohttp.web_urldispatcher import UrlDispatcher
from aiohttp import web

from utils import make_command, run_command

DEFAULT_METHODS = ('POST', 'GET')


class BaseCommandView:
    def __init__(self):
        self.methods = {}

        for method_name in DEFAULT_METHODS:
            method: Callable = getattr(self, method_name.lower(), None)
            if method:
                self.register_method(method_name, method)

    def register_method(self, method_name: str, method: Callable) -> None:
        self.methods[method_name.upper()] = method

    async def dispatch(self, request: Request):
        method = self.methods.get(request.method.upper())
        if not method:
            raise HTTPMethodNotAllowed('', DEFAULT_METHODS)
        path = request.match_info.copy()['path']
        if not path:
            raise HTTPBadRequest()
        kw = await request.json()

        return await method(*path.split('/'), **kw)


class CommandView(BaseCommandView):
    def __init__(self, resource: 'Resource'):
        super().__init__()
        self.resource = resource

    async def post(self, *args, **kwargs):
        # param1 = dict(request.rel_url.query)

        cmd = make_command(*args, **kwargs)
        response, returncode = await run_command(cmd)

        return web.json_response({'data': response})


class Resource:
    def __init__(self, prefix: str, *args):
        self.prefix = prefix
        self.endpoint = CommandView(self)

    def register(self, router: UrlDispatcher) -> None:
        router.add_route('*', '/{prefix}/{{path:.*}}'.format(
            prefix=self.prefix), self.endpoint.dispatch)

