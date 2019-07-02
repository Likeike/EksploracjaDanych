import re

class TextManipulator:
    test = "i&#039;ve tried a few antidepressants over the years (citalopram, fluoxetine, amitriptyline), but none of those helped with my depression, insomnia &amp; anxiety. my doctor suggested and changed me onto 45mg mirtazapine and this medicine has saved my life. thankfully i have had no side effects especially the most common - weight gain, i&#039;ve actually lost alot of weight. i still have suicidal thoughts but mirtazapine has saved me. my son has crohn&#039;s disease and has done very well on the asacol. he has no complaints and shows no side effects. he has taken as many as nine tablets per day at one time. i&#039;ve been very happy with the results, reducing his bouts of diarrhea drastically. quick reduction of symptoms contrave combines drugs that were used for alcohol, smoking, and opioid cessation. people lose weight on it because it also helps control over-eating. i have no doubt that most obesity is caused from sugar/carb addiction, which is just as powerful as any drug. i have been taking it for five days, and the good news is, it seems to go to work immediately. i feel hungry before i want food now. i really don&#039;t care to eat; it&#039;s just to fill my stomach. since i have only been on it a few days, i don&#039;t know if i&#039;ve lost weight (i don&#039;t have a scale), but my clothes do feel a little looser, so maybe a pound or two. i&#039;m hoping that after a few months on this medication, i will develop healthier habits that i can continue without the aid of contrave." \
           "i have been on this birth control for one cycle. after reading some of the reviews on this type and similar birth controls i was a bit apprehensive to start. im giving this birth control a 9 out of 10 as i have not been on it long enough for a 10. so far i love this birth control! my side effects have been so minimal its like im not even on birth control! i have experienced mild headaches here and there and some nausea but other than that ive been feeling great! i got my period on cue on the third day of the inactive pills and i had no idea it was coming because i had zero pms! my period was very light and i barely had any cramping! i had unprotected sex the first month and obviously didn&#039;t get pregnant so i&#039;m very pleased! highly recommend" \
           "4 days in on first 2 weeks. using on arms and face. put vaseline on lips, under eyes and in nostrils to protect from cream. so far no reaction at all. i know i have many pre cancer and thought i would light up like a christmas tree but so far so good. maybe it&#039;s coming but time will tell." \
           "i&#039;ve had the copper coil for about 3 months now. i was really excited at the thought of not taking hormones. i&#039;m good with pain however i nearly fainted with insertion, couldn&#039;t belive how painful it was; the doctor did say it is very painful for some. well 3 months in, my periods last 11 days and i&#039;m in pain for about 15 days with random twangs especially in the left side and i&#039;m considering whether i want to put up with the intense pain and heavy periods. i&#039;d recommend this 100% to somebody who doesn&#039;t already have heavy painful periods but right now it just isn&#039;t for me" \
           "this has been great for me. i&#039;ve been on it for 2 weeks and in the last week i only had 3 headaches which went away with 2 tylenol. i was having chronic daily headaches that wouldn&#039;t go away no matter what i took. i&#039;m still a little sleepy during the day, but i know that will get better. i take 10mg at night." \
           "ive been on methadone for over ten years and currently,i am trying to get off of this drug. ive been decreasing my does 2 mgs per month for over a year. i am at 3 mgs and really starting to feel the withdraw.i don&#039;t plan to get my next 30 doses.because its almost rediculous how little it does for me. i have 3 does doses of 3 mg and im terrified. can anyone give me some truthful encouragement?....." \
           "i was on this pill for almost two years. it does work as far as not getting pregnant however my experience at first was it didn&#039;t make a huge difference then 6 or 7 months into it my sex drive went down, along with being very very dry, my moodiness increased drastically. i would cry one second and then get angry with my husband over anything and everything. my skin has gotten a lot worse, i broke out in places i never had in the last week. so now i am on yaz." \
           "holy hell is exactly how i feel. i had been taking brisdelle for 1.5 years. the hot flashes did indeed subside - however, the side affects of this medicine coupled with the fact noven was acquired by yet another pharmaceutical company - you can&#039;t place a rep in the area, distribute your drugs, and then fire her-and not replace therefore there is no medicine or support here. you dumped this drug in the dr&#039;s hands and walked away. after calling sebula - " \
           "you act like you don&#039;t even care. you have made it impossible to obtain this. i happen to think this is illegal. i just decided to wean myself off this and premarin. it has been nothing short of a nightmare. if you don&#039;t need this drug- don&#039;t start. seriously. honestly its day one on the 3 day treatment. yes it burns a bit and it does leak out if you dont lay down after insertion. but im faithful it will work. this is a waste of money. did not curb my appetite nor did it make me feel full. no problems, watch what you eat."


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
        text = re.sub(r'(&[^;]{3,6};)|(but)|(why)|(where)|(good with pain)|(it burns)|[\'\./\?:-]', "", text)

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

        if good_count > bad_count :
            return 'good'
        elif good_count < bad_count:
            return 'bad'
        else:
            return '0'

