"""
Preprocessing text part 2 

case normalisation: onverting all of the text into lower case
stemming: removing a word's inflections to find the stem
punctuation and stop-word removal: stop-words are common functions words that in some situations can be ignored
"""
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
from itertools import zip_longest
import nltk
nltk.download('punkt')
nltk.download('twitter_samples')
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


# number normalisation
def number_normalise(token_input):
    token_input = (["NUM" if token.isdigit() else token for token in token_input])
    token_input = (["Nth" if not token.isalpha() and token.endswith(("th","rd","nd","st")) else token for token in token_input])
    return token_input

# make sentences lower case
def make_lower_case(input_sentences):
    lower_case_sentences = []
    for sentence in input_sentences:
        for word in sentence:
            lower_case_sentences.append(word.lower())
    return lower_case_sentences


# stemming
from nltk.stem.porter import PorterStemmer
st = PorterStemmer()

def get_stemmed(sentences):
    stemmed = []
    for sentence in sentences:
        for word in sentence:
            stemmed.append(st.stem(word))
    return stemmed

# lemmatization
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()

def lemmatize(word_list):
    for word in word_list:
        word = lem.lemmatize(word)
    return word_list

# stop word removal
from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stop_words(sentences):
    no_stop_words = []
    stop = stopwords.words('english')
    for sentence in sentences:
        for word in sentence:
            if word.isalpha() and word not in stop:
                no_stop_words.append(word)
    return no_stop_words