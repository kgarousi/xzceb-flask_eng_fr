""" french to english and english to french translator module"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """english to french translation"""
    translated = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return translated

def french_to_english(french_text):
    """french to english translation"""
    translated = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return translated
