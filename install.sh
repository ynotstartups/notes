#!/bin/bash

# remember to git clone git@github.com:ynotstartups/ynotstartups.github.io.git
# if `~/Documents/ynotstartups.github.io` doesn't exist

pip install --upgrade pip

pip install -r requirements.txt

pre-commit install

ln -f pre-push ./.git/hooks/pre-push
