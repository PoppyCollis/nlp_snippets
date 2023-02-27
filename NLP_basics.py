"""
NLP Basics

Author: Poppy Collis
    
"""

# get vocabulary
def get_vocab(any_text):
  words = any_text.lower()
  words = words.replace(",", "")
  words = words.split()
  vocab = set(words)
  return vocab

# dictionary of word frequencies
def create_dict(any_text):
  words = any_text.lower()
  words = words.replace(",","").replace(".","")
  words = words.split()
  dict1 = {}
  for word in words:
    if word in dict1.keys():
      dict1[word] += 1
    else:
      dict1[word] = 1
  return dict1

# files
"""
# google drive example
from google.colab import drive
drive.mount('/content/drive')
input_file_path='/content/drive/My Drive/Colab Notebooks/sample_text.txt'
"""
# use a with ... as block to open a file
 def print_word_counts(file_path):
  with open(file_path) as input_file:
    input_text = input_file.read()
    dictionary1 = create_dict(input_text)
    return dictionary1
