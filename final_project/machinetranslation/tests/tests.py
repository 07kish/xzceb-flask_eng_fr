import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):

    def test1(self):
        english_text = "Hello"
        english_to_french_text = english_to_french(english_text)
        self.assertEqual("", "")
        self.assertEqual(english_to_french_text, "Bonjour")
        

class TestFrenchToEnglish(unittest.TestCase):

    def test1(self):
        french_text = "Bonjour"
        french_to_english_text = french_to_english(french_text)
        self.assertEqual("", "")
        self.assertEqual(french_to_english_text, "Hello")

if __name__ == '__main__':
    unittest.main()