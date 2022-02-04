#!/bin/bash

### Check if a directory does not exist ###
if [ ! -d './venv' ]
then
    python3.10 -m venv .venv
fi

sudo apt-get update -y
sudo apt-get install -y exiv2

source .venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

ln -f pre-push ./.git/hooks/pre-push
