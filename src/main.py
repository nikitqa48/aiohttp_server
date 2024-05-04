from aiohttp import web
from hashapp.controller import routes
import click

app = web.Application()
app.add_routes(routes)


@click.command()
def main():
    click.echo(f"=======Сервер запущен http://localhost:8080 ========")
    return web.run_app(app, port=8080)


web = main()


