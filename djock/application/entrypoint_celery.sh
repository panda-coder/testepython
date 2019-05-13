#!/usr/bin/env bash
cd /app
pip3 install -r requirements.txt
celery --app=crawler.tasks worker --loglevel=INFO
