# Chess Server Capstone

## Purpose

Currently, a simple chess server designed to respond to 
requests for starting a game, making moves, and printing 
the state of the board. 

Stockfish is the engine used to determine the AI moves.

The serverapp/ directory contains the logic for all of the routes and
endpoints that exist in our server. The scripts/ directory contains the
script to play against the AI.

## Setup

### Installing Python 3.7

The first thing to do is install Python 3.7. That is currently the
version of Python being used to develop this project. Python 3.6 is
fine too but nothing lower since features in this project may break
it. 

If installing Python 3.7 on Windows, follow these steps:

- Download Python 3.7 from [link](https://www.python.org/downloads/)
- When the install window comes up, choose the option "Add Python 
  3.7 to PATH"
- To add Python permanently to your path so it could be executed anywhere
  follow the steps in this [link](https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path).
  Just change the Python27 to be Python37 or whatever it is specified as

### Virtual Environments

Installing a virtual environment is important to seperate the packages
used for different projects. 

Once you have attempted to use the python or python3.7 command in cmd prompt:

- Execute `python3 -m venv <venv_name>` where <venv_name> is whatever you want
  to call your virtual environment
- To run your virtual environment, execute `.\Scripts\activate` within the
  virtual environment directory
- To get out of the virtual environment from anywhere, just execute `deactivate`

If you activated your virtual environment, you should see the <venv_name> at the
beginning of your command prompt. Any packages installed through pip will show up
in this virtual environment and can only be used while the virtual environment is
active. If the environment is not activated, running code which depends on the
packages will result in errors. 

**REMEMBER TO ACTIVATE YOUR VIRTUAL ENVIRONMENT BEFORE RUNNING ANY OF THIS CODE.**

### Installing the Module

Now that we have Python and our virtual environments setup, we need to install
the package or the chess server in this case. 

First, clone the repository to your file system. This requires you to setup git
and a github profile. 

Once you have cloned the repository, move to the folder within the cmd prompt 
where the setup.py file exists, and execute `pip install -e .`. Remember to do 
this when your virtual environment is active. This command will install the 
package locally. 

Now that the package is setup locally, there are two command line scripts that are
also installed. The first is called run-chess-server which will start up the Flask
server and you can then send requests to. The second command is play_ai.py. This will
start up the file in scripts/play_ai.py. You can run this file from anywhere and it
will allow you to send requests to the server. **The server must be running for play_ai.py
to execute fully**.

Anytime you change the codebase, and want to test if everything works, remember to
re-run `pip install -e .` from within the folder where setup.py exists.


### Running the Code

Before running the code, even though I explained some steps to run it in the above 
section, you must change a few variables and complete an extra step. 

The config.py file contains some configuration values. You can change these based off
of your own values. The most important of which is the STOCKFISH_PATH. Install the 
Windows Stockfish Engine from this [link](https://stockfishchess.org/download/). 

Once the engine is downloaded, copy the absolute path for the engine and replace
the value for STOCKFISH_PATH in config.py. If using Windows, the use of the '\'
will break stuff since '\' is considered an escape character. In this case, add 
an r in front of the string (r'C:\Users\robing\...'). 

## Requirements

The Installing the Module section in Setup will automatically install the necessary
packages required for this. If you use other modules, add the module that you have
installed in the install_requires variable in setup.py as well as in the list below.

Required Packages:

- flask
- python-chess
- requests