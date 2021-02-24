# pandoc-latex-environment
![Python package](https://github.com/chdemko/pandoc-latex-environment/workflows/Python%20package/badge.svg?branch=develop)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-environment/1.1.6.svg)](https://coveralls.io/github/chdemko/pandoc-latex-environment?branch=1.1.6)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-environment.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-environment/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-environment.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-environment/1.1.6/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-environment.svg)](https://pypi.org/project/pandoc-latex-environment/)

*pandoc-latex-environment* is a [pandoc] filter for adding LaTeX environement on specific HTML `div` tags.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-latex-environment/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-latex-environment

Installation
------------

*pandoc-latex-environment* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-latex-environment* as root using the bash command

    pip install pandoc-latex-environment 

To upgrade to the most recent release, use

    pip install --upgrade pandoc-latex-environment 

To upgrade to the current code, use

    pip install --upgrade --force git+https://github.com/chdemko/pandoc-latex-environment

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

[python]: https://www.python.org/
[on Windows]: https://www.python.org/downloads/windows/
[PyPI]: https://pypi.python.org/pypi


Getting Help
------------

If you have any difficulties with *pandoc-latex-environment*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-environment/issues
