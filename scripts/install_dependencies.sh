#!/bin/bash

sudo apt-get update
#sudo apt-get install -y python2.7 python-pip
curl https://bootstrap.pypa.io/get-pip.py | sudo -H python3.6
pip3 install -r requirements.txt
pip install Flask
pip install gunicorn
pip install jinja2
