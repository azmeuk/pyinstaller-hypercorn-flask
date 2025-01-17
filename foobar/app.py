from flask import Flask
import click
import sys
from hypercorn.config import Config
from hypercorn.run import run as hypercorn_run
import multiprocessing

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@click.group()
def cli():
    pass


@cli.command()
def hello():
    print("Hello, world!")


@cli.command()
def runserver():
    print("Hypercorn runner starting...")

    config_obj = Config()
    config_obj.application_path = "foobar.app:app"
    exitcode = hypercorn_run(config_obj)

    print("Hypercorn runner stopped.")
    sys.exit(exitcode)


if __name__ == "__main__":
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        multiprocessing.freeze_support()

    cli()
