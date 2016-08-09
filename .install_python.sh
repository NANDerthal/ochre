curl https://bootstrap.pypa.io/get-pip.py | sudo -H python$PYTHON
python$PYTHON -m ensurepip
sudo -H pip$PYTHON install cython
sudo -H pip$PYTHON install -r requirements.txt

