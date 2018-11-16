import os
import torch
import numpy as np
import collections
np.random.seed(11)

class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = []
        self.vocab = []

    def add_word(self, word):
        self.vocab.append(word)

    def check_vocab(self, cutoff=30000):
        print 'Vocab length: ' + str(len(self.vocab))
        word_counter = collections.Counter(self.vocab)
        self.vocab_freq = word_counter.most_common(cutoff)
        self.vocab = [i[0] for i in self.vocab_freq]
        self.vocab.append('<unk>')
        for word in self.vocab:
            self.idx2word.append(word)
            self.word2idx[word] = len(self.idx2word) - 1
        return self.vocab

    def __len__(self):
        return len(self.idx2word)

class Dictionary_POS(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = []
        self.vocab = []

    def add_word(self, word):
        self.vocab.append(word)

    def check_vocab(self):
        print 'Vocab length: ' + str(len(self.vocab))
        word_counter = collections.Counter(self.vocab)
        self.vocab_freq = word_counter.most_common(cutoff)
        self.vocab = [i[0] for i in self.vocab_freq]
        for word in self.vocab:
            self.idx2word.append(word)
            self.word2idx[word] = len(self.idx2word) - 1
        return self.vocab

    def __len__(self):
        return len(self.idx2word)


class Corpus(object):
    def __init__(self, path):
        self.dictionary = Dictionary()
        self.dictionary_pos = Dictionary_POS()
        self.define_vocab(os.path.join(path, 'data.train'))
        self.train_text = self.tokenize(os.path.join(path, 'data.train'), type='train')
        self.valid_text = self.tokenize(os.path.join(path, 'data.dev'), type='eval')
        self.test_text = self.tokenize(os.path.join(path, 'data.test'), type='eval')


    def define_vocab(self, path):
        assert os.path.exists(path)
        # Add words to the dictionary

        self.dictionary.add_word('<eos>')
        with open(path, 'r') as f:
            tokens = 0
            for line in f:
                words = line.split() + ['<eos>']
                tokens += len(words)
                for word in words:
                    self.dictionary.add_word(word)
        vocab = self.dictionary.check_vocab()

        self.vocab_len = len(self.dictionary)
        print 'Final vocab len: ' + str(self.vocab_len)

    def define_vocab_pos(self, path):
        assert os.path.exists(path)
        # Add words to the dictionary

        self.dictionary.add_word('<eos>')
        with open(path, 'r') as f:
            tokens = 0
            for line in f:
                words = line.split() + ['<eos>']
                tokens += len(words)
                for word in words:
                    self.dictionary_pos.add_word(word)
        vocab = self.dictionary_pos.check_vocab()

        self.vocab_len = len(self.dictionary_poss)
        print 'Final vocab len: ' + str(self.vocab_len)

    def tokenize_pos(self, path):
        with open(path, 'r') as f:
            tokens = 0
            for line in f:
                words = line.split() + ['<eos>']
                tokens += len(words)
        # Tokenize file content
        with open(path, 'r') as f:
            ids = torch.LongTensor(tokens)
            token = 0

            for line in f:
                words = line.split() + ['<eos>']
                for idx, word in enumerate(words):
                    try:
                        ids[token] = self.dictionary.word2idx[word]
                    except:
                        ids[token] = self.dictionary.word2idx['<unk>']
                    token += 1

        return ids
    def tokenize(self, path, type='eval'):
        """Tokenizes a text file."""
        with open(path, 'r') as f:
            tokens = 0
            for line in f:
                words = line.split() + ['<eos>']
                tokens += len(words)

        # Tokenize file content
        with open(path, 'r') as f:
            ids = torch.LongTensor(tokens)
            token = 0

            for line in f:
                words = line.split() + ['<eos>']
                for idx, word in enumerate(words):
                    try:
                        ids[token] = self.dictionary.word2idx[word]
                    except:
                        ids[token] = self.dictionary.word2idx['<unk>']
                    token += 1

        return ids
