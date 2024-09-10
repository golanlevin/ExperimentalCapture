# Making a Virtual Environment

You may already have Homebrew and ffmpeg installed. Find out which versions you're running. I'm running Homebrew 4.3.20 and ffmpeg version 7.0.2.

* `brew --version`
* `ffmpeg -version`

If necessary, install Homebrew:

* `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

... and add Homebrew to your path:

* `(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/testuser/.zprofile`
* `eval "$(/opt/homebrew/bin/brew shellenv)"`

If necessary, install ffmpeg:

* `brew install ffmpeg`

Find out which version of Python is installed. I'm running Python 3.12.6.

* `python3 --version`

If necessary, you can install Python, e.g.:

* `brew install python@3.12`

Change directory to the folder in which you'd like to create your virtual environment(s). In my case, that looks like:

* `cd /Users/golan/Documents/dev/virtual_environments`

Create a new virtual environment in that directory. This will create a subdirectory (`myTestVenv `) containing various files.

* `python3.12 -m venv myTestVenv`

Activate the newly created virtual environment (You can exit the virtual environment later by typing `deactivate`):

* `source myTestVenv/bin/activate`

We will now install pipx (in the virtual environment), a tool that allows you to install Python applications in isolated environments. It can be installed with the following commands:

* `python3 -m pip install pipx`
* `python3 -m pipx ensurepath`

You can then ensure that pipx is properly installed by running this command:

* `pipx --version`