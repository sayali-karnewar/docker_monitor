from aiohttp import web
import asyncio
import aiohttp_jinja2
import jinja2

from routes import routes
from setup import setup

loop = asyncio.get_event_loop()
db = loop.run_until_complete(setup())

app = web.Application()
app['db'] = db

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))

routes(app)
web.run_app(app)