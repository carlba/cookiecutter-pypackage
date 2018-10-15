# coding=utf-8

from setuptools import setup, find_packages

setup(name="{{ cookiecutter.project_slug }}",
      version="{{ cookiecutter.version }}",
      options={},
      description="{{ cookiecutter.description }}",
      author="{{ cookiecutter.github_user }}",
      packages=find_packages(),
      install_requires=['click'],
      entry_points={'console_scripts': ['cookiecutter.project_slug = cookiecutter.project_slug.cli:main']}
)