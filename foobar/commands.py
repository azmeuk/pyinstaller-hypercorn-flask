import click
import sys
from hypercorn.config import Config
from hypercorn.run import run as hypercorn_run
from flask.cli import FlaskGroup
from foobar import app

@click.group(
    cls=FlaskGroup,
    create_app=lambda: app,
)
def cli():
    config_obj = Config()
    config_obj.application_path = "foobar:app"
    exitcode = hypercorn_run(config_obj)
    sys.exit(exitcode)

if __name__ == "__main__":
    cli()
