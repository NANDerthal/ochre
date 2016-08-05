# test graphics submodule

import unittest
import numpy as np

'''
from ochre import graphics

class TestSprite(unittest.TestCase):

    def test_loadSprite(self):
        self.assertEqual(true, true)

    def test_loadSprite(self):
        self.assertEqual(true, true)

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.camera = graphics.Camera()

    def resetCamera(self):
        self.camera.move(0, 0, 0)
        self.camera.lookAt(0, 0, 1)

    def test_constructor(self):
        self.assert(self.camera)
        self.assertEqual(self.camera.getPosition(), [0, 0, 0])
        self.assertEqual(self.camera.getLookAt(), [0, 0, 1])
        self.assertEqual(self.camera.getUp(), [0, 1, 0])
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_move(self):
        self.camera.move()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_lookAt(self):
        self.camera.lookAt()
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

    def test_strafeNone(self):
        resetCamera()
        self.camera.strafe(0, 0, 0)
        self.assertEqual(self.camera.getMatrix(), np.identity(4)

    def test_strafeX(self):
        resetCamera()
        self.camera.strafe(1, 0, 0)
        goal = np.identity(4)
        self.assertEqual(self.camera.getMatrix(), goal)

    def test_strafeY(self):
        resetCamera()
        self.camera.strafe(0, 1, 0)
        self.assertEqual(self.camera.getMatrix(), np.matrix(4))

    def test_strafeZ(self):
        resetCamera()
        self.camera.strafe(0, 0, 1)
        self.assertEqual(self.camera.getMatrix(), np.matrix(4))

    def test_strafeAll(self):
        resetCamera()
        self.camera.strafe(1, 1, 1)
        self.assertEqual(self.camera.getMatrix(), np.identity(4))

class TestShaderProgram(unittest.TestCase):

    def test_shaderProgram(self):
        self.assertEqual(true, true)
'''

def runGraphicsTests():
    #unittest.main()
    return True

