import re


class TextManipulator:

    @staticmethod
    def strip_spaces(text):
        return " ".join(text.split())

    @staticmethod
    def replace_words(text):
        words = {
            'not good': 'bad',
        }

        for oldWord, newWord in words.items():
            text = text.replace(oldWord, newWord);

        return text


