all: 
	echo $(TRAVIS_PYTHON_VERSION)
	python$(TRAVIS_PYTHON_VERSION) setup.py build_ext
	python$(TRAVIS_PYTHON_VERSION) setup.py install --user

# ===== TESTING ====

test-all:
	python$(TRAVIS_PYTHON_VERSION) tests/allTests.py

test-core:
	python$(TRAVIS_PYTHON_VERSION) tests/coreTests.py

test-graphics:
	python$(TRAVIS_PYTHON_VERSION) tests/graphicsTests.py

test-gui:
	python$(TRAVIS_PYTHON_VERSION) tests/guiTests.py

test-input:
	python$(TRAVIS_PYTHON_VERSION) tests/inputTests.py

test-physics:
	python$(TRAVIS_PYTHON_VERSION) tests/physicsTests.py

test-prototypes:
	python$(TRAVIS_PYTHON_VERSION) tests/prototypesTests.py

test-sound:
	python$(TRAVIS_PYTHON_VERSION) tests/soundTests.py

# ===== CLEANUP =====

clean:
	rm -rf build
	rm *.so
	rm ochre.cpp

