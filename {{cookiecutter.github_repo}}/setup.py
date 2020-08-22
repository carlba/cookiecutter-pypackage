# coding=utf-8

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as build_py_orig
import fnmatch

excluded = ['*test_*.py']


class BuildPyExclusions(build_py_orig):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return [
            (pkg, mod, file)
            for (pkg, mod, file) in modules
            if not any(fnmatch.fnmatchcase(file, pat=pattern) for pattern in excluded)
        ]


setup(name="{{ cookiecutter.project_slug }}",
      version="{{ cookiecutter.version }}",
      options={},
      description="{{ cookiecutter.description }}",
      author="{{ cookiecutter.github_user }}",
      packages=find_packages(exclude=['test.*']),
      cmdclass={'build_py': BuildPyExclusions},
      install_requires=['click'],
      entry_points={
          'console_scripts': [
              '{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.cli:cli'
          ]}
      )
