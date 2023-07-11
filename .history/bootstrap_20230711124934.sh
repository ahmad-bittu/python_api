#!/bin/sh
export FLASK_APP=./cashman/index.py
pipenv run flask --debug run -h 4.4.4.4