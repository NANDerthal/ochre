# deactivate travis virtualenv
deactivate
# set up tools
sudo apt-get --force-yes -y install libsdl2-dev
sudo apt-get --force-yes -y install libsdl2-ttf-dev
export PYTHON=$TRAVIS_PYTHON_VERSION
# make new virtualenv
virtualenv·venv·-p·python$PYTHON
#virtualenv --system-site-packages ./venv
echo "ls"
ls
echo "ls venv"
ls venv
echo "ls venv/bin"
ls venv/bin
. ./venv/bin/activate
export PYTHON=$TRAVIS_PYTHON_VERSION

