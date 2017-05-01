[![Build Status](https://travis-ci.org/RUGSoftEng/2017-Hestia-Server.svg?branch=development)](https://travis-ci.org/RUGSoftEng/2017-Hestia-Server)
# Hestia-Server 
Home automation, made simple again!

# General Description
This repository contains the server side code of the Hestia home automation
system.
The idea behind this project is to create a simple home automation system.
We strive to provide a platform that can extend to new types of peripherals  without
needing structural changes.
In the end, it should be possible for consumers to create their own plugins for
the system that allow the hestia platform to work with their peripherals as well.

Currently, we are in the development phase of this project.
What we have here is what we call our MVP.
It is a barebones system with one functional plugin, which is for the Philips Hue.
The current audience is still the homebrew and diy community that is willing to
do a little setup to get the system working.

The final goal is to make the hestia platform and thus the server easy to work
work with, secure and plug and play.

# Run the server

First, you run `dev_setup.sh` contained in the root directory of this project.
Then, you run `launch.sh` and you have running server.

# Development setup
To setup a development environments or to run the server you can follow these
steps.

First, you run `dev_setup.sh` contained in the root directory of this project.

Then, if you want to run the application from the command you first have to 
source the virtual environment activator.
If you have no idea where it is situated it is probably in its default location
so you run `source ~/.virtualenvs/hestia/bin/activate`.
If you changed the default location you probably know where to find it.
Then to run the application you run `python source/application.py` or `launch.sh`.

If you are using a pycharm as an IDE you need to go to `File | Settings | Project | Project Interpreter`
and select the virtual environment named "hestia".
Pycharm will take care of the rest.

# Usage
The server has a public REST api to interact with. 
Since we are still in the early beta stage (0.x.y version numbers) no guarantees
are made about the stability of the current api.
In other words, expect it to change in the near future.

To get an overview of the current public REST api it is best to start up an
instance of the server and to navigate to the port `8000`.
Here a nice swagger UI is shown similar to the picture below.
It shows the current state of the current API and allows you to interact with
the server.

![swagger_ui_screenshot](https://cloud.githubusercontent.com/assets/6391025/24971097/076699de-1fb7-11e7-8eed-a1ceccefe38f.png)


# Information
- [Virtual environment setup](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
- [Flask_restplus Framework Documentation](https://flask-restplus.readthedocs.io/en/stable/)
- [Flask Framework Documentation](http://flask.pocoo.org/)
- [Python tutorial for Java programmers](http://www.cse.wustl.edu/~ckelleher/cse450/pythonQuickStart.pdf)
