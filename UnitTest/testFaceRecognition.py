import unittest
import sys
lst = ["/home/user/", "/home/ehyeok9/github/"]
directory = lst[0]
sys.path.insert(0, directory + "Software-Project-II---AD-project/Face_Recognition")
from Facial_Recognition import FaceRecognition, FaceCapture
from PyQt5 import *

class testFaceRecognition(unittest.TestCase):

    def setUp(self):
        self.face = FaceRecognition("Kevin", "man")


    def testVariale(self):
        self.assertEqual(self.face.username, "Kevin")
        self.assertEqual(self.face.usergender, "man")
        self.assertTrue(self.face.isMan)

    def testUpdatData(self):
        self.assertEqual(len(self.face.userFiles), 100)

    def testCompareFace(self):
        self.assertIsNotNone(self.face.compare_face())
        

if __name__ == '__main__':
    unittest.main()
