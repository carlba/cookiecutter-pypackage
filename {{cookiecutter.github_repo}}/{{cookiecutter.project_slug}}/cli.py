# -*- coding: utf-8 -*-
"""Console script for {{cookiecutter.project_slug}}"""
import sys

import click
from click.testing import CliRunner

from . import core


def is_debugging():
    return not (sys.gettrace() is None)


@click.group()
def cli():
    pass


@cli.command()
def start():
    core.start()


@cli.command()
def stop():
    core.stop()


if __name__ == "__main__":
    if is_debugging():
        runner = CliRunner()
        runner.invoke(main)
    else:
        cli()
