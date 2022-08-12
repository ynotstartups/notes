#!/bin/bash

### Check if a directory does not exist ###
if [ ! -d './venv' ]
then
    python -m venv .venv
fi

source .venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

ln -f pre-push ./.git/hooks/pre-push
