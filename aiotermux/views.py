import json
import logging

from aiohttp.web_exceptions import HTTPMethodNotAllowed, HTTPBadRequest
from aiohttp.web import Request

DEFAULT_METHODS = ('POST', 'GET')


class BaseCommandView:
    def __init__(self):
        self.methods = {}

        for method_name in DEFAULT_METHODS:
            method = getattr(self, method_name.lower(), None)
            if method:
                self.register_method(method_name, method)

    def register_method(self, method_name, method):
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
    def __init__(self, resource):
        super().__init__()
        self.resource = resource


class Resource:
    def __init__(self, prefix, *args):
        self.prefix = prefix
        self.endpoint = CommandView(self)
