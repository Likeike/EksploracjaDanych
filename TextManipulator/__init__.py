
class TextManipulator:

    @staticmethod
    def strip_spaces(text):
        return " ".join(text.split())

    @staticmethod
    def replace_words(text):
        words = {
            'not good': 'bad',
            'not good': 'good',
        }

        for oldWord, newWord in words.items():
            text = text.replace(oldWord, newWord);

        return text

    @staticmethod
    def remove_unnecessary_words(text):
        words = ['but',  'why', 'where']

        for word in words :
            text = text.replace(word, '');

        return text


