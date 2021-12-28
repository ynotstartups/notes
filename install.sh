#!/bin/bash

sudo apt-get update -y
sudo apt-get install -y exiv2

source .venv/bin/activate

pip install -r requirements.txt

ln -f pre-commit ./.git/hooks/pre-commit
ln -f pre-push ./.git/hooks/pre-push
