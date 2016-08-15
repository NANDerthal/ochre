all:
	echo $(TRAVIS_PYTHON_VERSION)
	$(PYTHON) setup.py build_ext
	$(PYTHON) setup.py install --user

# ===== TESTING ====

test-all:
	$(PYTHON) tests/allTests.py

test-core:
	$(PYTHON) tests/coreTests.py

test-graphics:
	$(PYTHON) tests/graphicsTests.py

test-gui:
	$(PYTHON) tests/guiTests.py

test-event:
	$(PYTHON) tests/eventTests.py

test-physics:
	$(PYTHON) tests/physicsTests.py

test-prototypes:
	$(PYTHON) tests/prototypesTests.py

test-sound:
	$(PYTHON) tests/soundTests.py

# ===== CLEANUP =====

clean:
	rm -rf build
	rm *.so
	rm ochre.cpp

