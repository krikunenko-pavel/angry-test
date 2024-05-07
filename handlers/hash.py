import hashlib

from aiohttp import web

from models.hash import GenerateHashModel

router = web.RouteTableDef()


@router.post("/hash")
async def post(req: web.Request):
    data = GenerateHashModel.model_validate(await req.json())
    return web.json_response({
        "hash_string": hashlib.sha256(data.string.encode("utf-8")).hexdigest()
    })
