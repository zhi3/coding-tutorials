#!/bin/bash

set -e

vendor=tutorial
install_root="/opt/$vendor/"
build_dir=$(pwd)/build
rm -rf $build_dir
mkdir $build_dir

# NOTE we are not listing scandir here since we are currently pip installing
# it into the docker container, so there will be no apt package to depend
# on (yet).

fpm -s python -t deb \
    --python-install-bin ${install_root}/bin \
    --python-install-lib ${install_root}/lib/python2.7/site-packages/ \
    --no-python-dependencies \
    --python-install-data ${install_root}/conf/ \
    -d python-psutil \
    -d python-yaml \
    --workdir $build_dir \
    --vendor $vendor \
    -f setup.py
