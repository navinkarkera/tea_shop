#!/usr/bin/env bash

poetry install --no-dev
gunicorn backend.main:app -w 4 -k uvicorn.workers.UvicornWorker
