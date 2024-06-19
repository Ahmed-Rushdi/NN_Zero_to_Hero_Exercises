import torch
import torch.nn.functional as F
from abc import ABC, abstractmethod

class GramModel(ABC):
    def __init__(self, method='counts'):
        self.loss = None
        self._method = method if method in {'counts', 'nn'} else 'counts'
        self.bigrams = None
        self.stoi = None
        self.itos = None
        self.W = None

    def _get_mappings(self, bigrams):
        pass

    def _get_grams(self, corpus):
        bigrams = []
        for word in corpus:
            word = '. ' + word + '.'
            bigrams.append(*[(word[c], word[c + 1]) for c in range(len(word) - 1)])
        return bigrams

    def _fit_count(self, bigrams):
        pass

    def _fit_nn(self, bigrams):
        def fit(self, corpus, epochs=10):


class BigramModel :
    def __init__(self, method='counts'):
        self.loss = None
        self._method = method if method in {'counts', 'nn'} else 'counts'
        self.bigrams=None
        self.stoi=None
        self.itos=None
        self.W = None

    def _get_mappings(self, bigrams):
        pass

    def _get_grams(self, corpus):
        bigrams = []
        for word in corpus:
            word = '. ' + word + '.'
            bigrams.append(*[(word[c], word[c + 1]) for c in range(len(word) - 1)])
        return bigrams

    def _fit_count(self, bigrams):
        pass
    def _fit_nn(self, bigrams):
        pass
    def fit(self, corpus, epochs=10):
        pass


