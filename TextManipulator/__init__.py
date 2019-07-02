import re

class TextManipulator:
    @staticmethod
    def strip_spaces(text):
        return " ".join(text.split())

    @staticmethod
    def replace_words(text):

        text = re.sub(r'(not good)|(better)|(not bad)|(great)|(had no side effects)|(saved me)|' \
                     '(quick reduction of symptoms)|(It does work)|(helped me)|(allowed me to stay awake)|' \
                     '(cleared up my acne)|(drug is pretty amazing)|(no problem(s)?)|(happy)|(best)|(amazing)|(insane)|' \
                     '(very well)|(super)|(cool)|(fine)|(given me my life back)|(well)|' \
                     '((no|minimize) side effect(s)?)|(love this)|(recommend (it)? (to|for) everyone)|' \
                     '(no negative)|(positive)|(happy)|(happiest person ever)|(fantastic)|(works for me)|' \
                     '(nice)|(ok)|(okay)|(miracle)|(not that bad)|(recommend [^\s]* this)|(accept)|(brilliant)' \
                     '(wonderful)|(very effective)|(fabulous)|(genius)|(healed)|(impressive)|(love this)|(satisfied)|' \
                     '(outstanding)', 'good', text)

        text = re.sub(r'(not good)|(no reaction)|(no problems)|(waste of money)|(It didnt seem to have any effect)|'
                      r'(horrible breakouts)|(horrible acne)|(boobs would hurt)|(wired)|(less effective)|'
                      r'(least effective)|(didnt helped me)|(nightmare)|(horrible)|(this is not it)|'
                      r'(not very well)|(worst)|(not cool)|(not fine)|((was( a)?)? side effects are)|'
                      r'(not happy)|(painful)|(absolutely done taking this)|(will not be taking this any longer)|'
                      r'((dont|not) works for me)|(terrible)|(nothing to prevent)|(not ok)|(not okay)|(worse)|'
                      r'(massacre)|(suffering)|(not recommend)|(almost killed me)|(not impressive)|(angry)|(fail)|'
                      r'(hate)|(stupid)|(disappointed)|(dissatisfied)|(does not work)|(does not help)', 'bad', text)

        return text

    @staticmethod
    def remove_unnecessary_words(text):
        text = re.sub(r'(&[^;]{3,6};)|(but)|(why)|(where)|[\'\./\?:-]', "", text)

        return text

    @staticmethod
    def manipulate(text):
        text = text.lower()
        text = TextManipulator.strip_spaces(text)
        text = TextManipulator.remove_unnecessary_words(text)
        text = TextManipulator.strip_spaces(text)

        text = TextManipulator.replace_words(text)

        return text

    @staticmethod
    def count_result(text):
        goods_and_bads = re.findall(r'bad|good', text);
        good_count = goods_and_bads.count('good')
        bad_count = goods_and_bads.count('bad')

        if good_count > bad_count:
            return 'good'
        elif good_count < bad_count:
            return 'bad'
        else:
            return '0'

