#!/usr/bin/env bash
service nginx start
echo "Rainfall Service Starting"
uwsgi --ini uwsgi.ini
