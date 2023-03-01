# nlp_snippets
Collection of useful natural language processing code snippets. Use of NLTK library and Spacy.

**NLP basics**
- opening files
- getting vocabulary
- word frequency dictionaries

**Preprocessing text**

<em>Part 1</em>
- sentence segmentation
- word tokenization
- twitter corpus
- average sentence length in corpora

<em>Part 2</em>
- case normalisation
- stemming
- punctuation and stopword removal

**Jupyter Notebooks**

1. Sentiment Classification
Report on investigation of NLP methods for distinguishing positive and negative reviews written about movies. Comparison of a word list classifier approach to a Naive Bayes classifier.

2. POS tagging
This involves deciding the correct part-of speech tag (e.g., noun, verb, adjective etc) for each word in a sentence.  Since the correct tag for each word depends not only on the current word but on the tags of those words around it, it is generally viewed as a *sequence labelling* problem.  In other words, for a given sequence of words, we are asking what is the most likely sequence of tags?
 
3. Distributional semantics
In a distributional model of meaning, words are represented in terms of their co-occurrences. Notebook contrasts *close proximity* co-occurrence (where words co-occur, say, next to each other) with more *distant proximity* (where words co-occur, say, within a window of 10 words).

4. Information retrieval and Question answering
Involves finding relevant documents to a query expressed in terms of keywords and extracting keywords from a query

5. Named entity recognition
Notebook introduces the spaCy library (https://spacy.io/) which provides a number of very fast, state-of-the-art accuracy tools for carrying out NLP tasks including part-of-speech tagging, dependency parsing and named entity recognition.
