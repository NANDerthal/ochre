sudo apt-add-repository -y ppa:cython-dev/master-ppa
sudo apt-add-repository -y ppa:zoogie/sdl2-snapshots
sudo apt-get update

curl https://bootstrap.pypa.io/get-pip.py | sudo python
curl https://bootstrap.pypa.io/get-pip.py | sudo python3

export PATH=~/usr/bin:$PATH

