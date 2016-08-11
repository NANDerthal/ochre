echo $PYTHON
python$PYTHON --version
curl https://bootstrap.pypa.io/get-pip.py | sudo -H python$PYTHON
pip --version
sudo -H pip install cython
sudo -H pip install -r requirements.txt

