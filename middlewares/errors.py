import logging

from aiohttp import web
from pydantic_core._pydantic_core import ValidationError

logger = logging.getLogger(__name__)


async def error_middleware(
        _app: web.Application,
        handler
):
    async def middleware_handler(request):
        try:
            return await handler(request)
        except ValidationError as exc:
            logger.exception(exc)
            return handle_validation_error(exc)
        except web.HTTPException as exc:
            return default_error_handler(exc.status_code, exc)
        except Exception as exc:
            return default_error_handler(500, exc)

    return middleware_handler


def handle_validation_error(
        exc: ValidationError
) -> web.Response:
    return web.json_response(
        status=400,
        data={
            "validation_errors": str(exc)
        }
    )


def default_error_handler(
        status_code: int,
        exc: Exception
) -> web.Response:
    return web.json_response(
        status=status_code,
        data={
            "error": exc.__class__.__name__,
            "detail": str(exc)
        }
    )
