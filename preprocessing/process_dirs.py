import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from unidecode import unidecode
import string

DIR = '../data/supertextwiki/'
DIROUT = '../data/wikidata/'

dirs = [x[0] for x in os.walk(DIR)][1:]
print dirs
total_tokens = 0
tags = ['verb.cognition', 'verb.change', 'verb.body', 'verb.communication','verb.competition','verb.consumption',
'verb.contact','verb.creation','verb.emotion','verb.motion','verb.perception','verb.possession','verb.social','verb.stative','verb.weather',
'noun.act','noun.animal','noun.artifact','noun.attribute','noun.body','noun.cognition','noun.communication','noun.event','noun.feeling','noun.food',
'noun.group','noun.location','noun.motive','noun.object','noun.person','noun.phenomenon','noun.plant','noun.possession','noun.process',
'noun.quantity','noun.relation','noun.shape','noun.state','noun.substance','noun.time','noun.Tops']

def remove_non_ascii(text):
    printable = set(string.printable)
    return filter(lambda x: x in printable, text)
    # return unidecode(unicode(text, encoding = "utf-8"))
ssense_ = {}

def text2ptbformat(text):
    sent_tok = sent_tokenize(text)
    sentences = []
    for s in sent_tok:
        word_tokens = word_tokenize(s)
        sentences.append(' '.join(word_tokens))
    return ' '.join(sentences)


for i, dir in enumerate(dirs):
    # dir = x[0]
    print 'Processing dir no: ' + str(i+1)
    if i < 3:
        f1 = open(DIROUT + 'data.test', 'w')
        f2 = open(DIROUT + 'data.supersense.test', 'w')
        for files in os.listdir(dir):
            f = open(os.path.join(dir, files), 'r')
            whole_data = f.read().rstrip()
            whole_data = remove_non_ascii(whole_data)
            whole_data = text2ptbformat(whole_data).split()
            whole_data = ['unk' + w if w.startswith('_noun.') or w.startswith('_verb.') or w.startswith('_adj.') else w for w in whole_data]
            whole_data_ = ' '.join(['_'.join(w.split('_')[:-1]) if '_noun.' in w or '_adj.' in w or '_verb.' in w else w for w in whole_data])
            ssense = ' '.join([w.split('_')[-1] if '_noun.' in w or '_adj.' in w or '_verb.' in w else '<other>' for w in whole_data])
            assert len(whole_data_.split()) == len(ssense.split()), ' '.join(whole_data) + '\n' +  whole_data_ + '\n'+  "Sentence length mismatch"

            f1.write(whole_data_ + ' ')
            f2.write(ssense + ' ')

    elif i < 6:
        f1 = open(DIROUT + 'data.dev', 'w')
        f2 = open(DIROUT + 'data.supersense.dev', 'w')
        for files in os.listdir(dir):
            f = open(os.path.join(dir, files), 'r')
            whole_data = f.read().rstrip()
            whole_data = remove_non_ascii(whole_data)
            whole_data = text2ptbformat(whole_data).split()
            whole_data = ['unk' + w if w.startswith('_noun.') or w.startswith('_verb.') or w.startswith('_adj.') else w for w in whole_data]
            whole_data_ = ' '.join(['_'.join(w.split('_')[:-1]) if '_noun.' in w or '_adj.' in w or '_verb.' in w else w for w in whole_data])
            ssense = ' '.join([w.split('_')[-1] if '_noun.' in w or '_adj.' in w or '_verb.' in w else '<other>' for w in whole_data])

            assert len(whole_data_.split()) == len(ssense.split()), ' '.join(whole_data) + '\n' +  whole_data_ + '\n'+  "Sentence length mismatch"

            f1.write(whole_data_ + ' ')
            f2.write(ssense + ' ')

            # for s in sent:
            #     f1.write(s[:-1] + '\n')
    else:
        f1 = open(DIROUT + 'data.train', 'w')
        f2 = open(DIROUT + 'data.supersense.train', 'w')
        for files in os.listdir(dir):
            f = open(os.path.join(dir, files), 'r')
            # print os.path.join(dir, files)

            whole_data = f.read().rstrip()
            whole_data = remove_non_ascii(whole_data)
            whole_data = text2ptbformat(whole_data).split()
            total_tokens += len(whole_data)
            whole_data = ['unk' + w if w.startswith('_noun.') or w.startswith('_verb.') or w.startswith('_adj.') else w for w in whole_data]
            whole_data_ = ' '.join(['_'.join(w.split('_')[:-1]) if '_noun.' in w or '_adj.' in w or '_verb.' in w else w for w in whole_data])
            ssense = ' '.join([w.split('_')[-1] if '_noun.' in w or '_adj.' in w or '_verb.' in w else '<other>' for w in whole_data])

            assert len(whole_data_.split()) == len(ssense.split()), ' '.join(whole_data) + '\n' +  whole_data_ + '\n'+  "Sentence length mismatch"

            ssense__ = ssense.split()
            for s in ssense__:
                ssense_[s] = 0
            f1.write(whole_data_ + ' ')
            f2.write(ssense + ' ')
            # for s in sent:
            #     f1.write(s[:-1] + '\n')
print ssense_.keys()
print len(ssense_.keys())
print total_tokens
