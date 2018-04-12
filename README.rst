Word Embeddings Benchmarks
=====

.. image:: https://travis-ci.org/kudkudak/word-embeddings-benchmarks.svg?branch=master

Word Embedding Benchmark (web) package is focused on providing methods for easy evaluating and reporting
results on common benchmarks (analogy, similarity and categorization).

Research goal of the package is to help drive research in word embeddings by easily accessible reproducible
results (as there is a lot of contradictory results in the literature right now).
This should also help to answer question if we should devise new methods for evaluating word embeddings.

To evaluate your embedding (converted to word2vec or python dict pickle)
on all fast-running benchmarks execute `./scripts/eval_on_all.py <path-to-file>`.
See `here <https://github.com/kudkudak/word-embeddings-benchmarks/wiki>`_ results for embeddings available in the package.

Please also refer to our recent publication on evaluation methods https://arxiv.org/abs/1702.02170.

Disclaimer:

Package is currently under development, and we expect within next few months an official release. The main issue that might hit you at the moment is rather long embeddings loading times (especially if you use fetchers).

Features:

* scikit-learn API and conventions
* 17 popular datasets
* 11 word embeddings (word2vec, HPCA, morphoRNNLM, GloVe, LexVec, ConceptNet, HDC/PDC and others)
* methods to solve analogy, similarity and categorization tasks

Included datasets:

* WordRep
* Google Analogy
* MSR Analogy
* SemEval2012
* AP 
* BLESS
* Battig
* ESSLI (2b, 2a, 1c)
* WS353
* MTurk
* RG65
* RW
* SimLex999
* MEN

Note: embeddings are not hosted currently on a proper server, if the download is too slow consider downloading embeddings manually from original sources referred in docstrings.

Dependencies
======

Please see the requirements.txt and pip_requirements.txt file.

Install
======

First you may need to install the dependencies:

    pip install -r requirements.txt

For Wikipedia2Vec evaluation
========

| First, you need to have a glove-format wikipedia2vec model file to be evaluated. 
| You convert the model file using Wikipedia2vec's save_text method or word-embeddings-benchmarks/scripts/convert_wiki2vec_glove.py.

Convert your wikipedia2vec model file with convert_wiki2vec_glove.py::

    python scripts/convert_wiki2vec_glove.py [path to model file] [output file name]
   
Then evaluate your model by running scripts/evaluate_on_all.py::
    
    python scripts/evaluate_on_all.py --format glove --file [path to model file]
    
The model fils is assumed to be saved below $HOME/web_data. For example, if you have the model named wiki2vec_en_glove.txt,
the file should be in the directory $HOME/web_data/wiki2vec_en_glove.txt. 


When you would like to run the named entity benchmark (Kore)::

    python scripts/evaluate_on_all.py --format glove --file [path to model file] --entity True

The result is saved results.csv as default, and you can change the output file name by passing --output option.

Multilingual Word Embedding Evaluation
========
`Learning Word Vectors for 157 Languages (In proceedings of LREC 2018) <https://arxiv.org/pdf/1802.06893.pdf>`_
trained word vectors for 135 languages using Wikipedia and Common Crawl, and evaluate 10 major languages: 
Czech, German, Spanish, Finnish, French, Hindi, Italian, Polish, Portuguese and Chinese.

The original baseline results.

.. csv-table:: Performance of the various word vectors on word analogy tasks.
   :header: language, Cs, De, Es, Fi, Fr, Hi, It, Pl, Pt, Zh
   :widths: 10, 10, 10, 10,10, 10,10, 10,10, 10, 10

   "Accuracy[%]", 63.1, 61.0, 57.4, 35.9, 64.2, 10.6, 56.3, 53.4, 54.0, 62.0


The benchworks used for evaluation are below:

* Finish: `Finnish resources for evaluating language model semantics <https://github.com/venekoski/FinSemEvl>`_
* Czech: `New word analogy corpus for exploring embeddings of Czech words <https://github.com/Svobikl/cz_corpus>`_

* German: `Multilingual Reliability and “Semantic” Structure of Continuous Word Spaces <http://www.ims.uni-stuttgart.de/forschung/ressourcen/lexika/analogies_ims/analogies.en.html> `_
* Spanish: `Spanish Billion Words Corpus and Embeddings, <http://crscardellino.me/SBWCE/>`_
*Italy: `Word Embeddings Go to Italy: a Comparison of Models and Training Datasets <https://pdfs.semanticscholar.org/c38a/66bd7f71855e2e002331b55578c4c3606734.pdf>`_
* Portugese: `Portuguese Word Embeddings: Evaluating on Word Analogies and Natural Language Tasks <https://github.com/nathanshartmann/portuguese_word_embeddings>`_
* Chinese: `Joint Learning of Character and Word Embeddings <https://github.com/Leonard-Xu/CWE>`_

 
Examples
========
See `examples` folder.
The comparison between glove 100d and wikipedia2vec 100d: https://docs.google.com/spreadsheets/d/1-JQGkN8v5_xwqXeGpXu0CkdDlrSESENkV_oN7Xm_90Q/edit?usp=sharing

License
=======
Code is licensed under MIT, however available embeddings distributed within package might be under different license. If you are unsure please reach to authors (references are included in docstrings)

