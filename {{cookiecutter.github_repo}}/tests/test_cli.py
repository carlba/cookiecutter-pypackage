# -*- coding: utf-8 -*-
from click.testing import CliRunner

from {{cookiecutter.project_slug}}.cli import main


def test_start_returns_correct_output():
    runner = CliRunner()
    result = runner.invoke(start)
    assert 'Starting' in result.output

def test_stop_returns_correct_output():
    runner = CliRunner()
    result = runner.invoke(start)
    assert 'Stoppping' in result.output
