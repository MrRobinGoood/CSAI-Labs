import json_lines

from aiogram import Bot, Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import instruction
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re
import wikipedia
router = Router()
from lab1.clear_text import clear_str
wikipedia.set_lang("ru")
@router.message(Command('start'))
async def start(message: Message):
    await message.answer("Добро пожаловать в КСИИ Бот!")
    await message.delete()

@router.message()
async def messaging(message: Message):
    await message.answer(find_similar_answer(message.text))


dialogs = []
with open('./resources/dataset.jsonl', 'rb') as f:
    for item in json_lines.reader(f):
        question = item.get("question")
        answer = item.get("answer")
        if question is not None and answer is not None:
            dialogs.append((question, answer))
dialogs = dialogs[:30000]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([q + " " + a for q, a in dialogs])
y = np.array([i for i in range(len(dialogs))])


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В Википедии нет информации об этом'

def find_similar_answer(question):

    cq = clear_str(question)
    template = ['вики','википедия','wiki','wikipedia','вика']
    print(cq)
    for i in range(len(cq)):
        if cq[i] in template:
            return getwiki(' '.join(cq[i+1:]))
    else:
        query_vector = vectorizer.transform([question])
        distances = np.dot(X.toarray(), query_vector.toarray().T)
        nearest_idx = np.argmax(distances)
        similar_question, similar_answer = dialogs[nearest_idx]
        return similar_answer


