# -*- coding: utf-8 -*-
import numpy as np
from collections import defaultdict
from itertools import chain
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr

from wikipedia2vec import Wikipedia2Vec

ENTITY_CATEGORIES = {
    'it_companies': ['Apple Inc.', 'Google', 'Facebook', 'Microsoft', 'IBM'],
    'celebrities': ['Angelina Jolie', 'Brad Pitt', 'Johnny Depp', 'Jennifer Aniston', 'Leonardo DiCaprio'],
    'video_games': ['Grand Theft Auto IV', 'Quake (video game)', 'Deus Ex (series)', 'Guitar Hero (video game)', 'Max Payne'],
    'tv_series': ['The Sopranos', 'The A-Team', 'Futurama', 'The Wire', 'Mad Men'],
    'chuck_norris': ['Chuck Norris'],
}


def evaluate_on_Kore(w, dataset_file="web/datasets/rankedrelatedentities.txt"):
    dataset_obj = parse_dataset(dataset_file)

    results = defaultdict(list)
    category_mapping = {
        e: c for (c, l) in ENTITY_CATEGORIES.items() for e in l}

    for (title1, title_list) in dataset_obj.items():
        pred = []
        title_pairs = [title1]

        title1 = convert_title(title1).lower()
        try:
            vec1 = w[title1]
        except KeyError:
            print('Missing entity:' + title1)
            pred.append(0.0)
            continue

        for title2 in title_list:
            title_pairs.append(title2)
            title2 = convert_title(title2).lower()
            try:
                vec2 = w[title2]
            except KeyError:
                print('Missing entity:' + title2)
                pred.append(0.0)
                continue

            score = 1.0 - cosine(vec1, vec2)
            pred.append(score)

        correct = list(reversed(range(len(pred))))
        results[category_mapping[title_pairs[0]]].append(
            spearmanr(correct, pred)[0])

    print(results)

    return results


def convert_title(title):
    title_tokens = title.split()
    if len(title_tokens) == 1:
        return "ENTITY/" + title_tokens[0]
    else:
        return "ENTITY/" + "_".join(title_tokens)


def parse_dataset(dataset_file_path):
    target = None
    dataset_obj = defaultdict(list)
    f = open(dataset_file_path)
    dataset_file = f.readlines()
    for line in dataset_file:
        line = line.rstrip()
        if line.startswith('\t'):
            dataset_obj[target].append(line[1:])
        else:
            target = line

    return dataset_obj
