# Installation

[![Python package](https://github.com/chdemko/pandoc-latex-environment/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-latex-environment/actions/workflows/python-package.yml)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-environment/develop.svg)](https://coveralls.io/github/chdemko/pandoc-latex-environment?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-environment.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-environment/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-environment.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-environment/develop/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)
[![Poetry version](https://img.shields.io/badge/poetry-1.2%20|%201.3%20|%201.4%20|%201.5-blue.svg)](https://python-poetry.org/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1-blue.svg)](https://pandoc.org/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-environment.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-environment.readthedocs.io/en/latest/)

*pandoc-latex-environment* is a [pandoc] filter for adding LaTeX environement on specific HTML `div` tags.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-environment* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows].

Install *pandoc-latex-environment* using the bash command

~~~shell
$ pip install pandoc-latex-environment
~~~

To upgrade to the most recent release, use

~~~shell
$ pip install --upgrade pandoc-latex-environment 
~~~

To upgrade to the current code, use

~~~shell
$ pip install --upgrade --force git+https://github.com/chdemko/pandoc-latex-environment
~~~

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

~~~shell
$ apt-get install python3-pip
~~~

[python]: https://www.python.org/
[on Windows]: https://www.python.org/downloads/windows/
[PyPI]: https://pypi.python.org/pypi


Getting Help
------------

If you have any difficulties with *pandoc-latex-environment*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-environment/issues
