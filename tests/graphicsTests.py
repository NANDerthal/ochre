# test graphics submodule

import unittest
import numpy as np
from math import sqrt

from ochre import graphics

def matrixCompare(m1, m2):
    result = np.absolute(np.subtract(m1, m2))
    if(result.max > 0.00001):
        return False
    else:
        return True

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
        self.camera.setLookAt(0, 0, -1)
        self.camera.setUpVector(0, 1, 0)

    def generateMatrix(self, position, lookAt, upVector):
        zBasis = position - lookAt
        zBasis = zBasis / np.linalg.norm(zBasis)

        yBasis = upVector - np.dot(upVector, zBasis)
        yBasis = yBasis / np.linalg.norm(yBasis)

        xBasis = np.cross(yBasis, zBasis)

        expected = np.vstack((xBasis, yBasis, zBasis, np.zeros_like(xBasis)))
        expected = np.column_stack((expected, [0, 0, 0, 1]))

        return expected

    def checkMatrix(self):
        position = np.array(self.camera.getPosition())
        lookAt = np.array(self.camera.getLookAt())
        upVector = np.array(self.camera.getUpVector())

        expected = self.generateMatrix(position, lookAt, upVector):
        result = np.matrixCompare(self.camera.getMatrix(), expected))
        self.assertTrue(result)

    def test_constructor(self):
        self.assert(self.camera)
        self.assertEqual(self.camera.getPosition(), [0, 0, 0])
        self.assertEqual(self.camera.getLookAt(), [0, 0, -1])
        self.assertEqual(self.camera.getUpVector(), [0, 1, 0])
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    # camera set position

    def test_setPositionNone(self):
        self.resetCamera()
        self.camera.setPosition(0, 0, 0)
        self.checkMatrix()

    def test_setPositionX(self):
        self.resetCamera()
        self.camera.setPosition(0.5, 0, 0)
        self.checkMatrix()

    def test_setPositionY(self):
        self.resetCamera()
        self.camera.setPosition(0, 0.5, 0)
        self.checkMatrix()

    def test_setPositionZ(self):
        self.resetCamera()
        self.camera.setPosition(0, 0, 0.5)
        self.checkMatrix()

    def test_setPositionAll(self):
        self.resetCamera()
        self.camera.setPosition(-0.5, -0.5, -0.5)
        self.checkMatrix()

    # camera set lookAt

    def test_setLookAtNone(self):
        self.resetCamera()
        self.camera.setLookAt(0, 0, 0)
        self.checkMatrix()

    def test_setLookAtX(self):
        self.resetCamera()
        self.camera.setLookAt(1, 0, 0)
        self.checkMatrix()

    def test_setLookAtY(self):
        self.resetCamera()
        self.camera.setLookAt(0, 1, 0)
        self.checkMatrix()

    def test_setLookAtZ(self):
        self.resetCamera()
        self.camera.setLookAt(0, 0, 1)
        self.checkMatrix()

    def test_setLookAtAll(self):
        self.resetCamera()
        self.camera.setLookAt(1, 1, 1)
        self.checkMatrix()

    # camera set up vector

    def test_setUpVectorNone(self):
        self.resetCamera()
        self.camera.setUpVector(0, 0, 0)
        self.checkMatrix()

    def test_setUpVectorX(self):
        self.resetCamera()
        self.camera.setUpVector(1, 0, 0)
        self.checkMatrix()

    def test_setUpVectorY(self):
        self.resetCamera()
        self.camera.setUpVector(0, 1, 0)
        self.checkMatrix()

    def test_setUpVectorZ(self):
        self.resetCamera()
        self.camera.setUpVector(0, 0, 1)
        self.checkMatrix()

    def test_setUpVectorAll(self):
        self.resetCamera()
        self.camera.setUpVector(1, 1, 1)
        self.checkMatrix()

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

