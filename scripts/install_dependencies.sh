#!/bin/bash

sudo apt-get update
sudo apt-get install -y python2.7 python-pip
sudo apt-get install -y python3.6 python-pip
sudo apt-get install python3-pip
pip3 install -r requirements.txt

#pip install Flask
