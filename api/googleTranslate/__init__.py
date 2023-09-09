from googletrans import Translator

trans = Translator()


def translate_to_croatian(text: str):
    return trans.translate(text, src="en", dest="hr").text
