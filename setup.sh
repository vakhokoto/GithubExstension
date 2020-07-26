#!/bin/bash

# setup virtual environment
virtualenv -p python3 .
source bin/activate

# download django
pip3 install django==2.0.7

# get to front-end directory
cd src/my-app

# build front-end react project
sudo npm install
sudo npm install --save react-router-dom
npm run build

# return to home directory
cd ../..
