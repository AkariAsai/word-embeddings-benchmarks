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

Examples
========
See `examples` folder.
The comparison between glove 100d and wikipedia2vec 100d: https://docs.google.com/spreadsheets/d/1-JQGkN8v5_xwqXeGpXu0CkdDlrSESENkV_oN7Xm_90Q/edit?usp=sharing

License
=======
Code is licensed under MIT, however available embeddings distributed within package might be under different license. If you are unsure please reach to authors (references are included in docstrings)

