# test graphics submodule

import unittest
import numpy as np
from math import sqrt

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
        self.camera.setUpVector(0, 1, 0)

    def test_constructor(self):
        self.assert(self.camera)
        self.assertEqual(self.camera.getPosition(), [0, 0, 0])
        self.assertEqual(self.camera.getLookAt(), [0, 0, 1])
        self.assertEqual(self.camera.getUpVector(), [0, 1, 0])
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

    # camera set lookAt

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

    # camera set up vector

    def test_setUpVectorNone(self):
        self.resetCamera()
        self.camera.setUpVector()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setUpVectorX(self):
        self.resetCamera()
        self.camera.setUpVector()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setUpVectorY(self):
        self.resetCamera()
        self.camera.setUpVector()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setUpVectorZ(self):
        self.resetCamera()
        self.camera.setUpVector()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_setUpVectorAll(self):
        self.resetCamera()
        self.camera.setUpVector()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    # corner cases

    def test_lookAtEqualsPosition(self):
        self.resetCamera()
        self.camera.setPosition(0, 0, 0)
        self.camera.setLookAt(0, 0, 0)
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_lookAtEqualsUp(self):
        self.resetCamera()
        self.camera.setLookAt(0, 0, 0)
        self.camera.setUpVector(0, 0, 0)
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_positionEqualsUp(self):
        self.resetCamera()
        self.camera.setPosition(0, 0, 0)
        self.camera.setUpVector(0, 0, 0)
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_nonNormalizedUpVector(self):
        self.resetCamera()
        self.camera.setUpVector(42, 2, -93)
        expected = [42, 2, -93]
        magnitude = sum([x**2 for x in expected])
        expected = [x * sqrt(magnitude) for x in expected]
        self.assertEqual(self.camera.getUpVector(), expected ))

'''
class TestShaderProgram(unittest.TestCase):

    def test_shaderProgram(self):
        self.assertEqual(true, true)
'''

def runGraphicsTests():
    #unittest.main()
    return True

