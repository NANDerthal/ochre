echo $TRAVIS_PYTHON_VERSION
python$TRAVIS_PYTHON_VERSION --version
curl https://bootstrap.pypa.io/get-pip.py | sudo -H python$TRAVIS_PYTHON_VERSION
pip --version
sudo -H pip install cython
sudo -H pip install -r requirements.txt

