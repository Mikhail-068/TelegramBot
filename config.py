import nltk
from random import choice
from responses import BOT_CONFIG
import re

API_KEY = '5305576482'


def isMatch(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    pattern = r'[^\w\s]'
    text1 = re.sub(pattern, '', text1)
    text2 = re.sub(pattern, '', text2)


    if text1.find(text2) != -1:
        return True

    distance = nltk.edit_distance(text1, text2)
    length = (len(text1) + len(text1)) / 2
    score = round(distance / length, 2)

    return score < 0.4





def bot2(text, example, answer):
    text = text.lower()

    for ex in example:
        if isMatch(text, ex) == True:
            return choice(answer)



text = 'какая чудесная погода'

def Sonya(text):

    result = []
    for i in BOT_CONFIG["there's an answer"].values():
        result.append(bot2(text, i['question'], i['answer']))

    res = list(filter(lambda x: x!=None, result))


    if res == []: return choice(BOT_CONFIG['no answer'])
    else: return '! '.join(res)

