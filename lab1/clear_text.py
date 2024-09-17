import pandas as pd
from io import StringIO
from html.parser import HTMLParser
import re
from pymorphy3 import MorphAnalyzer
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

stopwords_ru = stopwords.words("russian")
morph = MorphAnalyzer()

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def remove_urls(text, replacement_text=""):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    text_without_urls = url_pattern.sub(replacement_text, text)
    return text_without_urls

def lemmatize(doc):
    patterns = "[0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-–•]+"
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        token = token.strip()
        token = morph.normal_forms(token)[0]
        if token not in stopwords_ru:
            tokens.append(token)
    return tokens

def clear_str(input_str):
    return lemmatize(input_str)
