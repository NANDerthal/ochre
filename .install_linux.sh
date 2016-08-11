# deactivate travis virtualenv
deactivate
# set up tools
sudo apt-get --force-yes -y install libsdl2-dev
sudo apt-get --force-yes -y install libsdl2-ttf-dev
PYTHON=$TRAVIS_PYTHON_VERSION
export PYTHON
echo Python version: $PYTHON
# make new virtualenv
#virtualenv·-p·python$PYTHON ./venv
#virtualenv --system-site-packages ./venv
#echo "ls"
#ls
#echo "ls venv"
#ls venv
#echo "ls venv/bin"
#ls venv/bin
#. ./venv/bin/activate
#export PYTHON=$TRAVIS_PYTHON_VERSION

