# -*- coding: utf-8 -*-
"""Console script for {{cookiecutter.project_slug}}."""
import click

import .{{ cookiecutter.project_slug }}

@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    main()