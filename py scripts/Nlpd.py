"""
Sriharsha Samala
"""

import json
import nltk
from nltk.stem.porter import PorterStemmer

class Nlpd(object):

    def __init__(self):
        self.name = "nlpd"
        self.docs = []
    
    @staticmethod
    def getTokens(text):
        """
        split text into individual tokens
        """
        tokens = nltk.word_tokenize(text)
        return tokens
    
    @staticmethod
    def getStems(tokens):
        """
        get stemmed tokens
        walking -> walk
        booked -> book
        """
        stemmer = PorterStemmer()
        stems = [stemmer.stem(token) for token in tokens]
        return stems
    
    @staticmethod
    def getTags(tokens):
        """
        get part of speech tags of tokens
        [token, pos]
        """
        pos = nltk.pos_tag(tokens)
        return pos

    @staticmethod
    def getEntities(tagged):
        """
        get entity tree of tagged tokens
        """
        entities = nltk.chunk.ne_chunk(tagged)
        return entities

    @classmethod
    def saveDoc(data):
        self.docs.push(data)