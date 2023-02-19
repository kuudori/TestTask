#!/usr/bin/env bash


DEFAULT_MODULE_NAME=src.main

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}

echo "Checking if Alembic has changes to make..."
if alembic check | grep -q 'New upgrade operations detected'
then
    echo "Alembic has changes to make. Making migrations and migrating..."
    alembic revision --autogenerate -m "New migration"
    alembic upgrade head
else
    echo "Alembic is already up to date with the database schema."
fi

exec  uvicorn --reload --proxy-headers --host $HOST --port $PORT "$APP_MODULE"

