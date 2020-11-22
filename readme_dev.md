

## Development environment Sanskrit Lexicon Documentation

These notes assume a Windows 10 computer with Gitbash and python3.4 or later.
It also assumes a previous version of the csldoc repository at Github.
These instructions describe a complete installation of development environment for csldoc on
local computer.

### initialize csldoc from github

```
git clone git@github.com:sanskrit-lexicon/csl-doc.git
cd csl-doc
```

### python requirements for sphinx
sphinx version 1.8.1 requirements:Python >=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*
I have python 2.7 and Python3.7 on local windows 10 computer.
Cologne website has python3.4.
On local computer, 'python3' is the command to run python3.7.   ('python' is command to run python2.7)
We must use python3.


### setup virtual environment with sphinx on local computer 

Be sure that 'csl-doc' is the current directory.  We are going to create subdirectories *virtualenv-16.0.0* and *myenv* within
csl-doc;  Note these are in .gitignore, so they are not tracked by git.
```
# 1. retrieve zipped version of virtualenv
# csl-doc is current directory
curl -O https://files.pythonhosted.org/packages/33/bc/fa0b5347139cd9564f0d44ebd2b147ac97c36b2403943dbee8a25fd74012/virtualenv-16.0.0.tar.gz
# 2. unpack the compressed file into directory virtualenv-16.0.0
tar xvfz virtualenv-16.0.0.tar.gz
# creates directory virtualenv-16.0.0
#3. Make a directory to contain a new virtual environment:
# use python3
python3 virtualenv-16.0.0/virtualenv.py myenv
# 4. activate the *myenv* virtual environment.  
source myenv/Scripts/activate
# When myenv is activated, the 'python' command refers to python3.7
 which python
#>>> /C/xampp/htdocs/cologne/csl-doc/myenv/Scripts/python

# note that this is python version 3.7, presumably since i used 'python3'
# in creating the virtual environment.
python --version
#>>> Python 3.7.0
# also check that 'pip' is also the one in 'myenv'
 which pip
#>>> /C/xampp/htdocs/cologne/csl-doc/myenv/Scripts/pip
#5. install sphinx
pip3 install sphinx
# Installing via `pip install sphinx` in my ubuntu machine downloaded 1.8.1.
# Therefore changed it to `pip3 install sphinx`, so that latest 2.1.2 version of sphinx is downloaded.
#6. Deactivate virtual environment
deactivate
#7. note on size:  myenv is 74MB
```

### quick commands for virtualenv
```
# in csl-doc directory
#1. Activate the 'myenv' virtual environment, so sphinx will be available
source myenv/Scripts/activate
# For Ubuntu machine, it is inside bin folder instead of Scripts folder. Use as shown below.
# source myenv/bin/activate
#2. Deactivate the 'myenv' viritual environment when you are done working with sphinx.
deactivate
```


### Steps used to initialize a new sphinx project
This section for information only.
*These were done initially. However they should NOT be redone.*  
The file 'source/conf.py' has some of these settings.  One which you might want to change is 'version'.
```
# be sure myenv is activated
# initalize sphinx document
sphinx-quickstart
# Choose to have  Separate source/build directories named 'source' and 'build'
#make copyright blank
#in source/conf.py, change 
#copyright = '2018, Jim Funderburk' to copyright = ''
This copyright seems to show on all pages.
When blank, there is still a copyright to Sphinx and alabaster.
Guess we'll have to leave these.
```

### Regenerate the documentation as html:
The 'build' directory is constructed or updated.
Note that the top-level html files is *build/index.html*.
The source files are in the *source* directory.
```
# be sure *myenv* is activated, csl-doc is current directory.
sphinx-build -b html source build

# Note on changes in sphinx version.  Note above that we installed sphinx in the virtual environment.
sphinx-build --version
# >>> 2.1.2  (as of June 26, 2019)
# When the files were generated previously (in Nov 11, 2018), sphinx-build was at version 1.8.1.
# The changes in sphinx-build from 1.8.1 to 2.1.2  generated many changes to the html generated output,
# even though we have not made any changes to the input files  (in directory *source*).
# >>> 2.2.1 (as of Nov 7, 2019).  
#  Again, many changes to output 
```

### Check output on local machine.
```
Under xampp, the browser url used is:
http://localhost/cologne/csl-doc/build/index.html
```

### Push to Github
``` 
# on local development machine, in csl-doc directory
git add .
git commit -m "Rebuild with latest version of sphinx (2.1.2)"
git push origin master
```

### Install at Cologne
Via ssh connection to Cologne,
```
# make current directory scans/csldev/csldoc
git pull origin master

```

