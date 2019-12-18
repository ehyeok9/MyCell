import unittest
import sys
lst = ["/home/user/", "/home/ehyeok9/github/"]
directory = lst[0]
sys.path.insert(0, directory + "Software-Project-II---AD-project/Face_Recognition")
from Facial_Recognition import FaceRecognition, FaceCapture
from PyQt5 import *
import numpy as np
from PIL import Image

class testFaceCapture(unittest.TestCase):

    def setUp(self):
        self.face = FaceCapture
        self.image = Image.open(directory + "Software-Project-II---AD-project/Face_Recognition/othersFaces/menFaces")
")
    def testFaceExtractor(self):
        self.assertIsNotNone(self.face.face_extractor(self.image))


if __name__ == '__main__':
    unittest.main()