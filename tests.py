


import unittest
#Own
import main

"""
class FileTemplteSaverTest(unittest.TestCase):
    def test_get_template_not_found_exception(self):
        with self.assertRaises(main.TemplateNotFoundException):
            saver = main.FileTemplateSaver()
            saver.get("second")
    def test_asset_equal_template_readlines(self):
        saver=main.FileTemplateSaver()
        self.assertEqual("{Person{\"name\":\"string\",\"last_name\":\"string\"}}\n",saver.get("first"))

class ClassFormatParsingTest(unittest.TestCase):
    def test_parsing_template(self):
        pass
    def test_parsing_array(self):
        pass

class ClassFormatSerializingTest(unittest.TestCase):
    def test_serializing_template(self):
        pass
    def test_serializing_array(self):
        pass
"""

#DESERIALIZATION
"""
class RemoveWhiteSpaceTest(unittest.TestCase):
    def test_removing_space(self):
        string="{\"name\":\"name1\" , \"last_name\": \"last_name1 \"}"
        aspected_string="{\"name\":\"name1\",\"last_name\":\"last_name1 \"}"
        self.assertEqual(main._remove_whitespace(string),aspected_string)
"""
class Test_load(unittest.TestCase):
    def test_load_file_not_found(self):
        pass


class Test_loads(unittest.TestCase):
    pass


class Test__get_value(unittest.TestCase):
    def test_whitespaces(self):
        input_str='  {"name": "name1"  , "last_name" :  "last_name1" } '
        aspected={"name":"name1","last_name":"last_name1"}
        self.assertEqual(main._get_value(input_str),aspected)


if __name__ == "__main__":
    unittest.main()
