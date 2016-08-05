all:
	

# ===== TESTING ====

test-all:
	python3 tests/allTests.py

test-core:
	python3 tests/coreTests.py

test-graphics:
	python3 tests/graphicsTests.py

test-gui:
	python3 tests/guiTests.py

test-input:
	python3 tests/inputTests.py

test-physics:
	python3 tests/physicsTests.py

test-prototypes:
	python3 tests/prototypesTests.py

test-sound:
	python3 tests/soundTests.py

# ===== TRAVIS-CI SETUP =====

# linux

before_install_linux:
	sudo apt-add-repository -y ppa:cython-dev/master-ppa
	sudo apt-add-repository -y ppa:zoogie/sdl2-snapshots
	sudo apt-get update
	export PATH=~/usr/bin:$PATH

install_linux:
	sudo apt-get --force-yes -y install libsdl2-dev
	sudo apt-get --force-yes -y install libsdl2-ttf-dev
	sudo apt-get --force-yes -y install cython3

# osx

before_install_osx:
	brew update
	brew install sdl2
	brew install sdl2_ttf
	brew install glew
	brew install glm
#	TODO: install SOIL

install_osx:
	brew install python3
	virtualenv venv -p python3
	source venv/bin/activate

