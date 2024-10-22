Installation
============

[![Python package](https://github.com/chdemko/pandoc-latex-environment/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-latex-environment/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-environment/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-environment?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-environment.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-environment/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-latex-environment/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-latex-environment/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-environment/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-environment)
[![Codacy](https://img.shields.io/codacy/grade/cf388bfa902c4afaaeae182594e5b38a.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-environment/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-environment.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-environment/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-environment.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-environment/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-environment.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-environment/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-environment?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-environment)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-environment.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-environment/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-environment.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-environment/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1%20|%203.2%20|%203.3%20|%203.4%20|%203.5-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-environment.svg?logo=github)](https://github.com/chdemko/pandoc-latex-environment/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-environment/develop?logo=github)](https://github.com/chdemko/pandoc-latex-environment/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-environment.svg?logo=github)](http://pandoc-latex-environment.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-environment.svg?logo=github)](http://pandoc-latex-environment.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-environment.svg?logo=koding&logoColor=white)](https://libraries.io/pypi/pandoc-latex-environment)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-environment.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-environment.readthedocs.io/en/latest/)

*pandoc-latex-environment* is a [pandoc] filter for adding LaTeX environement
on specific pandoc `div`.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-environment* requires [python], a programming language that
comes pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-latex-environment* using the bash command

~~~shell-session
$ pipx install pandoc-latex-environment
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-environment
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI]. It can be installed
using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org/
[on Windows]: https://www.python.org/downloads/windows/
[PyPI]: https://pypi.python.org/pypi


Getting Help
------------

If you have any difficulties with *pandoc-latex-environment*,
please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-environment/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

