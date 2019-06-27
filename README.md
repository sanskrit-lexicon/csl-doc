# csldoc
Development version of cologne sanskrit lexicon 'documentation'


### sphinx
The documentation is generated with the [sphinx python documentation generator](http://www.sphinx-doc.org/en/master/).

This repository contains all the sphinx source code, as well as the resulting build output.

The [readme_dev](https://github.com/sanskrit-lexicon/csldoc/blob/master/readme_dev.me) document describes how to
set up a development environment.  Some pieces of the development environment are *not* included in the repository:
* virtualenv-16.0.0 directory for local installation of virtualenv
* myenv directory, the python virtual environment containing the sphinx library.

### motivation for repository
Recently, an additional element  (@fxru translation of Grassman preface) arose and needed to be added to the
documentation.  The original development of the documentation (2014) existed only on my local
computer.  Since I now have more experience with Github and how to integrate github repositories with the
Cologne web site, it was a clear choice to put this self-contained unit here on Github.

~~As of this writing,  the form of the documentation built from this repository is not quite finished; in particular
the Cologne web site is still using the 2014 version.~~
