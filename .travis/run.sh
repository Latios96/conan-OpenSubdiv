#!/bin/bash

set -e
set -x

#conan create . Latios96/stable
export UPLOAD_URL=https://api.bintray.com/conan/latios96/my_conan
python3 build.py
