from aiohttp import web

from handlers import (
    hash,
    healthcheck
)


def add_routes(app: web.Application):
    app.router.add_routes(healthcheck.router)
    app.router.add_routes(hash.router)
    return app
