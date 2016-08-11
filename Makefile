all: 
	python$(PYTHON) setup.py build_ext
	python$(PYTHON) setup.py install --user

# ===== TESTING ====

test-all:
	python$(PYTHON) tests/allTests.py

test-core:
	python$(PYTHON) tests/coreTests.py

test-graphics:
	python$(PYTHON) tests/graphicsTests.py

test-gui:
	python$(PYTHON) tests/guiTests.py

test-input:
	python$(PYTHON) tests/inputTests.py

test-physics:
	python$(PYTHON) tests/physicsTests.py

test-prototypes:
	python$(PYTHON) tests/prototypesTests.py

test-sound:
	python$(PYTHON) tests/soundTests.py

# ===== CLEANUP =====

clean:
	rm -rf build
	rm *.so
	rm ochre.cpp

