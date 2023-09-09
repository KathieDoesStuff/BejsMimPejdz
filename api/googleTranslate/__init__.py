from googletrans import Translator

translator = Translator()


def translate_to_croatian(text: str):
    return translator.translate(text, src="en", dest="hr").text
