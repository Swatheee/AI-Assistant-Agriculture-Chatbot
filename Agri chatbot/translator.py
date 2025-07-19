from googletrans import Translator

def detect_language(text):
    translator = Translator()
    lang = translator.detect(text).lang
    return lang

def translate_text(text, target_lang="en"):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text
