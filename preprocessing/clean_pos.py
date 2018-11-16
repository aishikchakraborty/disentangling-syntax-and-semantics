import json
import os
import argparse

parser = argparse.ArgumentParser(description='Wikipedia-2018 Corpus')
parser.add_argument('--data-dir', type=str, default='../data/wikidata/annotated/',
                    help='location of the data corpus')
parser.add_argument('--data', type=str, default='data.train.json',
                    help='part of dataset used')
parser.add_argument('--output-dir', type=str, default='../data/wikidata/',
                    help='part of dataset used')
args = parser.parse_args()

data = json.loads(open(os.path.join(args.data_dir, args.data), 'r').read().strip('\n'))
f = open(os.path.join(args.output_dir, 'data.pos.' + args.data.split('.')[1]), 'w')
for i, sent in enumerate(data['sentences']):
    print 'Processing sentence: ' + str(i)
    pos = []
    for tokens in sent['tokens']:
        pos.append(tokens['pos'])
    f.write(' '.join(pos) + ' ')
