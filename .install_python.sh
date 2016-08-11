python$PYTHON --version
curl https://bootstrap.pypa.io/get-pip.py | sudo -H python$PYTHON
pip-$PYTHON --version
sudo -H pip-$PYTHON install cython
sudo -H pip-$PYTHON install -r requirements.txt

