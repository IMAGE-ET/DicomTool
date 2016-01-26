import unittest
import json

from HelperFunctions import HelperFunctions


class TestStringMethods(unittest.TestCase):

    def test_Json_dict_to_annotation_object(self):
        """
            test JSON to annotation list method
        """
        helper_functions = HelperFunctions()
        json_string = """[
                {
                    "endX": 1300, 
                    "endY": 592, 
                    "startX": 1222, 
                    "startY": 416, 
                    "title": "bone"
                }
        ]"""

        annontation_test_list = json.loads(json_string, object_hook=helper_functions.JsonDictToAnnotationObject)
        self.assertEqual(annontation_test_list[0].title, 'bone')
        self.assertEqual(annontation_test_list[0].endX, 1300)

    def test_get_zoom_zcale(self):
        """
            test zoom scaling
        """
        helper_functions = HelperFunctions()
        zoom_scale = helper_functions.getZoomScale(80, 35, 40, 40)
        self.assertEqual(zoom_scale, 2)

if __name__ == '__main__':
    unittest.main()
