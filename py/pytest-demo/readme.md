## Python demo
* pytest
* setuptools
* fpm: to build a deb for ubuntu

Run Command:
```
$ bash -x packages.sh
$ sudo dpkg -i *.deb
$ export PYTHONPATH=/opt/tutorial/lib/python2.7/site-packages/
$ /opt/tutorial/bin/pydemo
App.__init__
View.__init__
result: 1, 2
```
