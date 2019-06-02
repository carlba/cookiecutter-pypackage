# -*- coding: utf-8 -*-
"""Console script for {{cookiecutter.project_slug}}"""
import sys

import click
from click.testing import CliRunner

from . import core


def is_debugging():
    return not (sys.gettrace() is None)


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    if is_debugging():
        runner = CliRunner()
        runner.invoke(main)
    else:
        main()
