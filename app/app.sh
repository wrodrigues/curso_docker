#!/bin/sh
pip uninstall psycopg2
pip install bottle==0.12.13
pip install psycopg2-binary
pip install redis
python -u sender.py