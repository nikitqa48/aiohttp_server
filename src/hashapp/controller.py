from aiohttp import web
from .form import FormData
from .service import HashService
from json import JSONDecodeError

routes = web.RouteTableDef()


@routes.get('/healthcheck')
async def healthcheck(request: web.Request):
    return web.json_response(status=200, data={})


@routes.post('/hash')
async def hash(request: web.Request):
    try:
        data = await request.json()
        form = FormData(**data)
        return web.json_response(status=200, data={'hash_string': HashService().hash(form.string)})
    except (TypeError, JSONDecodeError):
        error = {'validation_errors': 'post data must be json and contain string field'}
        return web.json_response(status=400, data=error)

