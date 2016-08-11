echo $TRAVIS_PYTHON_VERSION
python --version
curl https://bootstrap.pypa.io/get-pip.py | sudo -H python
pip --version
sudo -H python -m pip install cython
sudo -H python -m pip install -r requirements.txt

