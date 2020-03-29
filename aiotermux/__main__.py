from aiohttp import web

from views import Resource


if __name__ == '__main__':
    app = web.Application()
    resource = Resource('api')
