import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_null_french_to_english(self):
        self.assertEqual(french_to_english(""),"")

    def test_null_english_to_french(self):
        self.assertEqual(english_to_french(""),"")

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

if __name__=='__main__':
    unittest.main()
