#! /bin/bash
# A script that downloads all the necessary files, setups the raspberry pi
# so that all necessary dependencies are installed. 
# And finally run the server.

# Install all the dependencies normally not installed by default
# on the raspberry pi.
sudo apt-get update
sudo apt-get install -y virtualenv \
                        build-essential \
                        libssl-dev \
                        libffi-dev \
                        python3-dev
                    
# Get the latest source code of the Hestia server
wget https://github.com/RUGSoftEng/2017-Hestia-Server/archive/master.zip
unzip master.zip
cd 2017-Hestia-Server-master

# Setup virtual python environment for the server
source ./dev_setup.sh
source ./launch.sh
