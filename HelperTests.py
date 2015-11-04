import unittest
import json

from AnnotationObject import AnnotationObject
from HelperFunctions import HelperFunctions

class TestStringMethods(unittest.TestCase):

    def test_JsonDictToAnnotationObject(self):
        """
            test JSON to annotation list method
        """
        helperFunctions = HelperFunctions()
        jsonString = """[
                {
                    "endX": 1300, 
                    "endY": 592, 
                    "startX": 1222, 
                    "startY": 416, 
                    "title": "bone"
                }
        ]"""

        annotationTestList = json.loads(jsonString, object_hook=helperFunctions.JsonDictToAnnotationObject)
        self.assertEqual(annotationTestList[0].title, 'bone')
        self.assertEqual(annotationTestList[0].endX, 1300)

    def test_getZoomScale(self):
        """
            test zoom scaling
        """
        helperFunctions = HelperFunctions()
        zoomScale = helperFunctions.getZoomScale(80, 35, 40, 40)
        self.assertEqual(zoomScale, 2)

if __name__ == '__main__':
    unittest.main()