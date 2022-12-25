#!/bin/bash

# remember to git clone git@github.com:ynotstartups/ynotstartups.github.io.git
# if `~/Documents/ynotstartups.github.io` doesn't exist

# install venv, ubuntu doesn't come it
sudo apt install python3.10-venv

### Check if a directory does not exist ###
if [ ! -d './venv' ]
then
    python -m venv .venv
fi

source .venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

ln -f pre-push ./.git/hooks/pre-push
