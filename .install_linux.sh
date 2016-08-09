# deactivate travis virtualenv
deactivate
# set up tools
sudo apt-get --force-yes -y install libsdl2-dev
sudo apt-get --force-yes -y install libsdl2-ttf-dev
export PYTHON=$TRAVIS_PYTHON_VERSION
# make new virtualenv
virtualenv --system-site-packages ./testvenv
echo "ls"
ls
echo "ls testvenv"
ls testvenv
echo "ls testvenv/bin"
ls testvenv/bin
. ./testvenv/bin/activate

