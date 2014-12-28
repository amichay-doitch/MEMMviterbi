import numpy as np
import math
from features import F
import logging
from tags import TAGS
_logger = logging.getLogger("utils")



def file2sentences(file):
    """
        input: path to file
        output: list of tuples, each tuple -([list of words], [list of tags])
    """
    sentence = []
    tags = []
    sentence_tags = []
    #f = open(file, 'r')
    alist = [line.rstrip() for line in open(file, 'r')]
    for line in alist:
        if not line:
            sentence_tags.append((sentence, tags))
            sentence = []
            tags = []
            continue
        s_line = line.split(" ")
        tags.append(s_line[0])
        sentence.append(s_line[1])
    sentence_tags.append((sentence, tags))
    for sentence, tags in sentence_tags:
        if len(sentence) != len(tags):
            _logger.error('In sentence {0} \n\t\tthere is different number of '
                            'sentences and tags. sentences={1},tags={2}'.format(sentence, len(sentence), len(tags)))
    return sentence_tags

def scalar_product(a, b):
    return np.inner(a, b)

def probability(t_2, t_1, sentence, i, t, V):
    """
    :param V: tuned coefficients Vector
    :param history: list of tuples, each tuple -([list of words], [list of tags])
    :return: exp(V*F)/(sum over t exp(V*F)
    """
    numerator = math.exp(np.inner(V, F(t_2, t_1, sentence, i, t)))
    denominator = 0
    for tag in TAGS:
        denominator += math.exp(np.inner(V, F(t_2, t_1, sentence, i, tag)))
    return numerator/denominator
