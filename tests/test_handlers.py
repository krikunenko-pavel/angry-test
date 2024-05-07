import hashlib
import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_healthcheck(cli):
    res = await cli.get("/healthcheck")
    logger.info(res)
    assert res.status == 200
    assert await res.json() == {}


@pytest.mark.asyncio
@pytest.mark.parametrize("param", ["test_string", "string", "asgasasdgas"])
async def test_hash(cli, param):
    res = await cli.post("/hash", json={
        "string": param
    })

    assert res.status == 200
    assert (await res.json()).get("hash_string") == hashlib.sha256(param.encode("utf-8")).hexdigest()


@pytest.mark.asyncio
async def test_empty_request(cli):
    res = await cli.post("/hash", json={})

    assert res.status == 400
    assert (await res.json()).get("validation_errors")
