""" def count_words(text):
    # Split words on spaces.
    counts = {}
    W = text.lower().replace('\n', ' ').split(' ')
    for w in W:
        if w != '':
            if w in counts:
                counts[w] += 1
            else:
                counts[w] = 1

    return counts """

import collections
import re


def count_words(text):
    """Split words on spaces."""
    counts = collections.defaultdict(int)
    # Reemplza all \s con space y divide por ' '
    words = re.sub(r"\s+", " ", text.lower()).split(' ')
    for word in words:
        counts[word] += 1
    return counts


def count_words_in_file(in_file, out_file):
    """
    No se exploro pero toma un archivo
    y saca otro
    """
    with open(in_file, 'r') as f:
        counts = count_words(f.read())

    with open(out_file, 'w') as f:
        for word, count in counts.items():
            f.write(f"{word},{count}\n")
