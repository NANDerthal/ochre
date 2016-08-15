# test graphics submodule

import unittest
import numpy as np
from math import sqrt

import constants

from ochre import graphics

# test matrix equality within allowable tolerance
# note: some error is expected due to the differences in OpenGL type precision
def matrixCompare(m1, m2):
    result = np.absolute(np.subtract(m1, m2))
    if(result.max > constants.FLOAT_TOLERANCE):
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

    # Instantiate camera object
    def setUp(self):
        self.camera = graphics.Camera()

    # ===== Utility functions for tests =====

    # set camera back to default position
    def resetCamera(self):
        self.camera.setPosition(0, 0, 0)
        self.camera.setLookAt(0, 0, -1)
        self.camera.setUpVector(0, 1, 0)

    # create correct matrix based on input vectors
    def generateMatrix(self, position, lookAt, upVector):
        # get the z-axis vector for an orthonormal basis
        # we take z-axis to mean the distance from the image plane, where the camera
        # faces towards the negative z-direction
        # thus, we use negative the direction in which the camera is facing
        zBasis = position - lookAt
        zBasis = zBasis / np.linalg.norm(zBasis)

        # get the y-axis vector for an orthonormal basis
        # we want this to be in the up direction of the image plane
        # thus, we use the up vector from the camera
        yBasis = upVector - np.dot(upVector, zBasis)
        yBasis = yBasis / np.linalg.norm(yBasis)

        # get the x-axis vector for an orthonormal basis
        # this is found by taking the cross product of the orthonormalized x and y vectors
        xBasis = np.cross(yBasis, zBasis)

        # create a change of basis matrix by stacking the basis vectors
        expected = np.vstack((xBasis, yBasis, zBasis, np.zeros_like(xBasis)))
        # convert the matrix to use homogeneous coordinates
        expected = np.column_stack((expected, [0, 0, 0, 1]))

        return expected

    # compare camera output to expected output
    def checkMatrix(self):
        position = np.array(self.camera.getPosition())
        lookAt = np.array(self.camera.getLookAt())
        upVector = np.array(self.camera.getUpVector())

        expected = self.generateMatrix(position, lookAt, upVector)
        result = np.matrixCompare(self.camera.getMatrix(), expected)
        return result

    # ===== Actual test functions =====

    def test_constructor(self):
        self.assertNotEqual(self.camera, None)
        self.assertEqual(self.camera.getPosition(), [0, 0, 0])
        self.assertEqual(self.camera.getLookAt(), [0, 0, -1])
        self.assertEqual(self.camera.getUpVector(), [0, 1, 0])
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    # camera set position

    def test_setPositionNone(self):
        self.resetCamera()
        self.camera.setPosition(0, 0, 0)
        self.assertTrue(self.checkMatrix())

    def test_setPositionX(self):
        self.resetCamera()
        self.camera.setPosition(0.5, 0, 0)
        self.assertTrue(self.checkMatrix())

    def test_setPositionY(self):
        self.resetCamera()
        self.camera.setPosition(0, 0.5, 0)
        self.assertTrue(self.checkMatrix())

    def test_setPositionZ(self):
        self.resetCamera()
        self.camera.setPosition(0, 0, 0.5)
        self.assertTrue(self.checkMatrix())

    def test_setPositionAll(self):
        self.resetCamera()
        self.camera.setPosition(-0.5, -0.5, -0.5)
        self.assertTrue(self.checkMatrix())

    # camera set lookAt

    def test_setLookAtNone(self):
        self.resetCamera()
        self.camera.setLookAt(0, 0, 0)
        self.assertTrue(self.checkMatrix())

    def test_setLookAtX(self):
        self.resetCamera()
        self.camera.setLookAt(1, 0, 0)
        self.assertTrue(self.checkMatrix())

    def test_setLookAtY(self):
        self.resetCamera()
        self.camera.setLookAt(0, 1, 0)
        self.assertTrue(self.checkMatrix())

    def test_setLookAtZ(self):
        self.resetCamera()
        self.camera.setLookAt(0, 0, 1)
        self.assertTrue(self.checkMatrix())

    def test_setLookAtAll(self):
        self.resetCamera()
        self.camera.setLookAt(1, 1, 1)
        self.assertTrue(self.checkMatrix())

    # camera set up vector

    def test_setUpVectorNone(self):
        self.resetCamera()
        self.camera.setUpVector(0, 0, 0)
        self.assertTrue(self.checkMatrix())

    def test_setUpVectorX(self):
        self.resetCamera()
        self.camera.setUpVector(1, 0, 0)
        self.assertTrue(self.checkMatrix())

    def test_setUpVectorY(self):
        self.resetCamera()
        self.camera.setUpVector(0, 1, 0)
        self.assertTrue(self.checkMatrix())

    def test_setUpVectorZ(self):
        self.resetCamera()
        self.camera.setUpVector(0, 0, 1)
        self.assertTrue(self.checkMatrix())

    def test_setUpVectorAll(self):
        self.resetCamera()
        self.camera.setUpVector(1, 1, 1)
        self.assertTrue(self.checkMatrix())

    # corner cases

    def test_lookAtEqualsPosition(self):
        # expect degenerate case
        self.resetCamera()
        self.camera.setPosition(0.5, 0.5, 0.5)
        self.camera.setLookAt(0.5, 0.5, 0.5)
        self.assertEqual(self.camera.getMatrix(), np.zeros(4,4))

    def test_lookAtEqualsUp(self):
        # expect degerate case
        self.resetCamera()
        self.camera.setLookAt(0, 0, 1)
        self.camera.setUpVector(0, 0, 1)
        self.assertEqual(self.camera.getMatrix(), np.zeros(4,4))

    def test_positionEqualsUp(self):
        # expect normal case (up is a vector, not a position)
        self.resetCamera()
        self.camera.setPosition(0.5, 0.5, 0.5)
        self.camera.setUpVector(0.5, 0.5, 0.5)
        self.assertTrue(self.checkMatrix())
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_zeroUpVector(self):
        # expect degenerate case
        self.resetCamera()
        self.camera.setUpVector(0, 0, 0)
        self.assertEqual(self.camera.getMatrix(), np.zeros(4,4))

    def test_nonNormalizedUpVector(self):
        # expect to normalize input vector
        self.resetCamera()
        self.camera.setUpVector(42, 2, -93)
        expected = [42, 2, -93]
        magnitude = sum([x**2 for x in expected])
        expected = [x * sqrt(magnitude) for x in expected]
        self.assertEqual(self.camera.getUpVector(), expected)

    def test_movePositionPastLookAt(self):
        # expect to point 'backwards' relative to start position
        self.resetCamera()
        self.setPosition(0, 0, 2)
        self.assertTrue(self.checkMatrix())

'''
class TestShaderProgram(unittest.TestCase):

    def test_shaderProgram(self):
        self.assertEqual(true, true)
'''

def runGraphicsTests():
    #unittest.main()
    return True

