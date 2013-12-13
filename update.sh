#!/bin/sh
pip install -r requirements_loose.txt
pip freeze >| requirements.txt
python manage.py syncdb
python manage.py migrate