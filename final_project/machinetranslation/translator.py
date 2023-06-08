""" This module contains 2 functions translating string text fr-en """
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """ This module translates string text en->fr """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """ This module translates string text en<-fr """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text
