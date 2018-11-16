import os
import argparse
import corenlpy

parser = argparse.ArgumentParser(description='Wikipedia-2018 Corpus')
parser.add_argument('--data-dir', type=str, default='../data/wikidata/',
                    help='location of the data corpus')
parser.add_argument('--data', type=str, default='data.train',
                    help='part of dataset used')
parser.add_argument('--output-dir', type=str, default='../data/wikidata/annotated/',
                    help='part of dataset used')
args = parser.parse_args()

# f = open(os.join(args.data_dir, args.data), r)
corenlpy.corenlp(
        in_files=[os.path.join(args.data_dir, args.data)],
        out_dir=args.output_dir,
        annotators=['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse'],
        threads=8,
        output_format='json'
    )
