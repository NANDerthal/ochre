# test graphics submodule

import unittest
import numpy as np

from ochre import graphics

'''
class TestSprite(unittest.TestCase):

    def test_loadSprite(self):
        self.assertEqual(true, true)

    def test_loadSprite(self):
        self.assertEqual(true, true)
'''

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.camera = graphics.Camera()

    def resetCamera(self):
        self.camera.setPosition(0, 0, 0)
        self.camera.setLookAt(0, 0, 1)
        self.camera.setOrientation(0, 1, 0)

    def test_constructor(self):
        self.assert(self.camera)
        self.assertEqual(self.camera.getPosition(), [0, 0, 0])
        self.assertEqual(self.camera.getLookAt(), [0, 0, 1])
        self.assertEqual(self.camera.getOrientation(), [0, 1, 0])
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    # camera set position

    def test_setPositionNone(self):
        self.resetCamera()
        self.camera.setPosition()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setPositionX(self):
        self.resetCamera()
        self.camera.setPosition()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setPositionY(self):
        self.resetCamera()
        self.camera.setPosition()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setPositionZ(self):
        self.resetCamera()
        self.camera.setPosition()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setPositionAll(self):
        self.resetCamera()
        self.camera.setPosition()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    # camera setLookAt

    def test_setLookAtNone(self):
        self.resetCamera()
        self.camera.setLookAt()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setLookAtX(self):
        self.resetCamera()
        self.camera.setLookAt()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setLookAtY(self):
        self.resetCamera()
        self.camera.setLookAt()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setLookAtZ(self):
        self.resetCamera()
        self.camera.setLookAt()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setLookAtAll(self):
        self.resetCamera()
        self.camera.setLookAt()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    # camera set orientation

    def test_setOrientationNone(self):
        self.resetCamera()
        self.camera.setOrientation()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setOrientationX(self):
        self.resetCamera()
        self.camera.setOrientation()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setOrientationY(self):
        self.resetCamera()
        self.camera.setOrientation()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setOrientationZ(self):
        self.resetCamera()
        self.camera.setOrientation()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setOrientationAll(self):
        self.resetCamera()
        self.camera.setOrientation()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    # corner cases

    def test_overlappingArguments(self):
        self.resetCamera()
        self.camera.setPosition(0, 0, 0)
        self.camera.setLookAt(0, 0, 0)
        self.camera.setOrientation(0, 0, 0)
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

'''
class TestShaderProgram(unittest.TestCase):

    def test_shaderProgram(self):
        self.assertEqual(true, true)
'''

def runGraphicsTests():
    #unittest.main()
    return True

