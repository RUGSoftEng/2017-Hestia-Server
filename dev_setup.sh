#!/usr/bin/env bash
################################################################################
# dev_setup.sh
#
# The purpose of this script is to create a self contained development 
# environment using virtualenv for python dependency sandboxing. This script 
# will create a virtualenv (using the conventions set by virtualenv-wrapper for
# location and naming) and install the requirements laid out in requirements.txt
#
# This script is an adaption of an already consisting script for mycroft-core.
# And the original author of this script is:
#  @author sean.fitzgerald (aka clusterfudge)
# We have changed it to meet the needs of this project.
################################################################################

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

# create virtualenv, consistent with virtualenv-wrapper conventions
if [ ! -d ${VIRTUALENV_ROOT} ]; then
   mkdir -p $(dirname ${VIRTUALENV_ROOT})
  virtualenv -p python3 ${VIRTUALENV_ROOT}
fi
source ${VIRTUALENV_ROOT}/bin/activate
cd ${TOP}
easy_install pip==9.0.1 # fjrce version of pip
pip3 install --upgrade virtualenv

# install requirements (except pocketsphinx)
pip3 install -r requirements.txt 
