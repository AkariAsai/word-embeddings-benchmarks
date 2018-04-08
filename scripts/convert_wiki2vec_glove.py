'''
This is a script to convert a wikipedia2vec model file to word2vec.
Usage:
$ python3 convert_wiki2vec_glove.py [MODEL_NAME] [OUTPUT_FILE_NAME]
'''
from wikipedia2vec import Wikipedia2Vec
from wikipedia2vec.dictionary import Word
import sys


def save_text(wiki2vec, out_file):
    with open(out_file, 'wb') as f:
        for item_idx, item in enumerate(sorted(wiki2vec.dictionary, key=lambda o: o.doc_count, reverse=True)):
            vec_str = ' '.join('%.4f' % v for v in wiki2vec.get_vector(item))
            if isinstance(item, Word):
                text = item.text.replace('\t', ' ')
            else:
                text = 'ENTITY/' + item.title.replace('\t', ' ')

            ext = text.replace(' ', '_')

            f.write(('%s %s\n' % (text, vec_str)).encode('utf-8'))


def main():
    argvs = sys.argv
    argc = len(argvs)

    MODEL_FILE = argvs[1]
    OUTPUT_FILE = argvs[2]
    wiki2vec = Wikipedia2Vec.load(MODEL_FILE)
    save_text(wiki2vec, OUTPUT_FILE)


if __name__ == "__main__":
    main()
