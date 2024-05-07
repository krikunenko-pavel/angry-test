import logging

from aiohttp import web

from handlers import add_routes
from middlewares.errors import error_middleware

logger = logging.getLogger(__name__)


async def factory():
    logger.info("Build App")
    return add_routes(web.Application(middlewares=[error_middleware]))
