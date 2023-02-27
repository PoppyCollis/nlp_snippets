"""
Preprocessing Text Part 1

- sentence segmentation: grouping characters into sentences
- word tokenisation: grouping characters into words
"""

import sys
import re
import pandas as pd
from itertools import zip_longest

import nltk
nltk.download('punkt')
# can use interactive download if using google colab or jupyter
# select 'd' for download and then 'l' for list, you can see all of the NLTK resources available
# nltk.download()

# 1) sentence segmentation with sent_tokenize
from nltk.tokenize import sent_tokenize

with open(input_file_path) as input:
    input_text = input.read()
    a = sent_tokenize(input_text)
    print(a)
    
# 2) NLTK regular expression tokenizer with word_tokenize
from nltk.tokenize import word_tokenize
#Arguments: a single string, representing a sentence
#Returns: a list of strings, where each string is a token within the sentence
# better than the .split() function
test_sentence="The cat sat on the mat."
word_tokenize(test_sentence) 

# 3) corpora
nltk.download('reuters')
from nltk.corpus import reuters

# print some sentences
sents = reuters.sents()
sample_size = 10
for s in sents[1:10]:
    print(len(s))
    
# note that type(sents) = nltk.corpus.reader.util.ConcatenatedCorpusView Object
"""
A 'view' of a corpus file acts like a sequence of tokens:
it can be accessed by index, iterated over, etc.  However, the
tokens are only constructed as-needed -- the entire corpus is
never stored in memory at once.
"""

# 4) random sampling of sentences
import random
random.seed(33) # can set a seed if I like

def sample_sentences(corpus,sample_size):
    size=len(corpus)
    ids=random.sample(range(size),sample_size) 
    sample=[corpus[i] for i in ids]  #this is an example of a list comprehension
    return sample

sample_sentences(reuters.sents(), 3)

# function which prints n sample sentences from twitter corpus
nltk.download('twitter_samples')
from nltk.corpus import twitter_samples

tweets = twitter_samples.strings() # these are accessed via .strings() method rather than .sents()
sample_size_n = 21
for s in tweets[0:sample_size_n]:
    print(s)   
    
# sample of random tweets
def get_tweets(num_tweets):
    tweets = twitter_samples.strings()
    size = len(twitter_samples.strings())
    rand_nums = random.sample(range(size), num_tweets)
    sample=[tweets[i] for i in rand_nums]
    return sample


# The twitter text doesn't come pre-tokenised
# Code to generate a list of list of tokens for your sample
tweets = get_tweets(10)
tokenized_tweets = [word_tokenize(tweets_sample[i]) for i in range(len(tweets_sample))]

# get average length of sentence

def sample_sentences(corpus,sample_size):
    if corpus == twitter_samples:
        corpus = corpus.strings()
    else:
        corpus = corpus.sents()
    size=len(corpus)
    ids=random.sample(range(size),sample_size)
    total_len=[]
    for i in ids:
        sample=corpus[i] 
        total_len.append(len(sample))
    av_len= sum(total_len) / sample_size
    return av_len

sample_sentences(reuters, 2)