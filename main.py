import click
from aiohttp import web

from app import factory


@click.command()
@click.option("--host", default="0.0.0.0", help="App Host")
@click.option("--port", default=8000, help="App Port")
def main(
        host: str,
        port: int,
):
    web.run_app(
        app=factory(),
        host=host,
        port=port,
    )


if __name__ == "__main__":
    main()
