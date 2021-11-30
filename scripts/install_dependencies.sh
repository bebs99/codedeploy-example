#!/bin/bash

sudo apt-get update
sudo apt-get install -y python2.7 python-pip
sudo curl https://bootstrap.pypa.io/get-pip.py | python3.6 - --user
pip3 install -r requirements.txt

#pip install Flask
