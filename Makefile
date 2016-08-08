all: 
	python3 setup.py build_ext
	python3 setup.py install --user

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

# ===== CLEANUP =====

clean:
	rm -rf build
	rm *.so
	rm ochre.cpp

