#!/usr/bin/env bash

PROJECTNAME="hestia"

# exit on any error
set -Ee

if [ $(id -u) -eq 0 ]; then
  echo "This script should not be run as root or with sudo."
  exit 1
fi

TOP=$(cd $(dirname 0) && pwd -L)

if [ -z "$WORKON_HOME" ]; then
    VIRTUALENV_ROOT=${VIRTUALENV_ROOT:-"${HOME}/.virtualenvs/$PROJECTNAME"}
else
    VIRTUALENV_ROOT="$WORKON_HOME/$PROJECTNAME0"
fi

source ${VIRTUALENV_ROOT}/bin/activate

python source/application.py run