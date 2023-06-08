import unittest

from translator import english_to_french, french_to_english

class TestTranslate(unittest.TestCase):
    def testEnglishToFrench(self): 
        self.assertEqual(english_to_french('Good morning'), 'Bonjour') # Test for the translation of the word ‘Good morning’ and ‘Bonjour’.
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')     # Test for the translation of the word ‘Hello and ‘Bonjour’.
    def testFrenchToEnglish(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')       # Test for the translation of the word ‘Bonjour’ and ‘Hello’.
        self.assertNotEqual(french_to_english('Salut'), 'Hello')      # Test for the translation of the word ‘Salut’ and ‘Hello’.
unittest.main()