'''
Used to run all tests from local machine.
(CI runs tests individually)
'''

from coreTests import runCoreTests
from graphicsTests import runGraphicsTests
from guiTests import runGuiTests
from inputTests import runInputTests
from physicsTests import runPhysicsTests
from prototypesTests import runPrototypesTests
from soundTests import runSoundTests

def main():
    print("RUNNING CORE TESTS")
    assert runCoreTests(), "CORE TESTS FAILED!"

    print("RUNNING GRAPHICS TESTS")
    assert runGraphicsTests(), "GRAPHICS TESTS FAILED!"

    print("RUNNING GUI TESTS")
    assert runGuiTests(), "GUI TESTS FAILED!"

    print("RUNNING INPUT TESTS")
    assert runInputTests(), "INPUT TESTS FAILED!"

    print("RUNNING PHYSICS TESTS")
    assert runPhysicsTests(), "PHYSICS TESTS FAILED!"

    print("RUNNING SOUND TESTS")
    assert runSoundTests(), "GUI SOUND FAILED!"

    print("ALL TESTS PASSED!")

main()

