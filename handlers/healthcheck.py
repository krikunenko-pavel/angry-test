from aiohttp.web import (
    RouteTableDef,
    json_response
)

router = RouteTableDef()


@router.get("/healthcheck")
async def handle(request):
    return json_response({})
