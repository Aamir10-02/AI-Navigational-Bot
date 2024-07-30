import numpy as np
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):

    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    word_freq = {word: 0 for word in all_words}


    for word in tokenized_sentence:
        if word in word_freq:
            word_freq[word] += 1

    
    bag_of_words_vector = np.array([word_freq[word] for word in all_words], dtype=np.float32)

    return bag_of_words_vector




# def bag_of_words(tokenized_sentence, all_words):
#     """
# sentence = ['which', 'type', 'of', 'work', 'do', 'you', 'do?']
# words = ["hi", "hello", 'of', "I", "you", "bye",'which', 'type', 'work', 'do', 'you', 'do?', "thank", "cool"]
# bag = bag_of_words(sentence, words)
# print(bag)
#     bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
#     """
#     tokenized_sentence = [stem(w) for w in tokenized_sentence]

#     # bag = np.zeros(len(all_words), dtype=np.float32)
#     # for idx, w in enumerate(all_words):
#     #     if w in tokenized_sentence:
#     #         bag[idx] = 1.0
    
#     # return bag