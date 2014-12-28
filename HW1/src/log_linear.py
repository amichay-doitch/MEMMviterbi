import sys
import math
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import fmin_l_bfgs_b
from utils import file2sentences, probability, scalar_product, TAGS
from features import F
import logging
from viterbi import viterbiAlgo
import time
import operator
import random
import array
_logger = logging.getLogger("log_linear")
_logger.setLevel(logging.DEBUG)

#FILE = "..\data\sample.txt"
#FILE = "..\data\GENIA_dmcc_pos.txt"
GOLDFILE = "..\data\sec2-21_first_5000_pos.txt"
LAMBDA = 0.05
BEST = [float("inf")]
results = {}

def logLinearLost(X0, args):
    """
    :param X0: vector (to be tuned by an algorithm)
    :param args: sentence_tags: list of tuples, each tuple -([list of words], [list of tags])
    :return: lost value
    """
    start_time = time.time()
    # if str(X0) in results:
    #     print str(X0), 'in the table:', results[str(X0)]
    #     return results[str(X0)]
    # else:
    #     print X0,

    sentence_tags = args
    firstSigma = 0.0
    secondSigma = 0.0
    for X, Y in sentence_tags:
        for i in range(len(X)):
            t_2, t_1, sentence, i = get_history(i, X, Y)
            firstSigma += np.inner(X0, F(t_2, t_1, sentence, i, Y[i]))
            secondSigma += math.log(expSumOverTags(X0, t_2, t_1, sentence, i))

    thirdSigma = np.inner(X0,X0)
    thirdSigma = float(thirdSigma) * LAMBDA / 2
    result = -(firstSigma - secondSigma - thirdSigma)
    # results[str(X0)] = result
    print "runtime: {4};firstSigma={0},secondSigma={1},thirdSigma={2},L(V)={3}".format(
        firstSigma, secondSigma, thirdSigma, result, time.time()-start_time)
    if result < BEST[0]:
        BEST[0] = result
        xo = ",".join([str(t) for t in X0])
        _logger.info(xo)
    return result


def f_prime(X0, args):
    print "f_prime"
    t1 = time.time()
    sentence_tags = args
    firstSigma = 0.0
    secondSigma = 0.0
    for X, Y in sentence_tags:
        for i in range(len(X)):
            t_2, t_1, sentence, i = get_history(i, X, Y)
            firstSigma += np.inner(X0, F(t_2, t_1, sentence, i, Y[i]))
            secondSigma += sum_f_over_prob(X0, t_2, t_1, sentence, i)
    sig = firstSigma - secondSigma
    der = map(operator.sub, [sig]*len(X0),X0*LAMBDA)
    der = np.array(der)
    print der
    print time.time() - t1
    return der



def sum_f_over_prob(X0, t_2, t_1, sentence, i):
    sum = 0
    for t in TAGS:
        sum += np.inner(X0, F(t_2, t_1, sentence, i, t)) * probability(t_2, t_1, sentence, i, t, X0)
    return sum



def expSumOverTags(V, t_2, t_1, sentence, i):
    sum = 0
    for t in TAGS:
        sum += math.exp(np.inner(V, F(t_2, t_1, sentence, i, t)))
    return sum

def get_history(i, X, Y):
    if i == 0:
        t_2 = t_1 = "*"
    elif i == 1:
        t_2 = "*"
        t_1 = Y[i-1]
    else:
        t_2 = Y[i-2]
        t_1 = Y[i-1]

    #history = (t_2, t_1, X, i)
    return t_2, t_1, X, i


def run_fmin_l_bfgs_b(sentence_tags):
    _logger.info("Enter to run_fmin_l_bfgs_b")
    #history = 'DT', 'NN', 'The dog jumps dog jumps', 2
    vector = F('DT', 'NN', 'The dog jumps dog jumps', 2, 't')
    print len(vector)
    X0 = [0] * len(vector)
    v = fmin_l_bfgs_b(logLinearLost,  np.array(X0), args=(sentence_tags,),  approx_grad=True, disp=5)
    #X0 = [random.random()] * len(vector)
    #v = fmin_l_bfgs_b(logLinearLost,  np.array(X0), args=(sentence_tags,),  fprime=f_prime, disp=5)

    print v
    return v

def rum_minimize(sentence_tags):
    #v = minimize(logLinearLost, [0, 0], args=(sentence_tags,), method='BFGS')
    bounds = ((None, None), (None, None), (None, None))
    options = {
        "maxiter": 2,
        "disp": True,
        "maxcor": 3,
        }
    v = minimize(logLinearLost,  np.array([0, 0, 0]), args=(sentence_tags,), method='BFGS', options=options)#, bounds=bounds)

def viterbiCheck():
    sentence_tags = file2sentences(GOLDFILE)
    V = [-5.96877389,  2.11503551, 3.5078505]
    s = sentence_tags[0][0]
    print s
    print " ".join(s)
    print viterbiAlgo(" ".join(s), V)
#249045.364516



def main():
    sentence_tags = file2sentences(GOLDFILE)
    run_fmin_l_bfgs_b(sentence_tags)




def trash():
    V = [-5.96877389, 2.11503551, 3.5078505]
    sentence_tags = file2sentences(GOLDFILE)
    s_t = sentence_tags[1]
    print s_t[0]
    print s_t[1]
    for i in range(len(s_t[0])):

        history = get_history(i, s_t[0], s_t[1])
        print history
        print probability(V, get_history(i, s_t[0], s_t[1]),s_t[1][i])
        a = input("Enter a number")

def print_all_tags():
    sentence_tags = file2sentences(GOLDFILE)
    tagsSet = set()
    for words, tags in sentence_tags:
        for POS in tags:
            tagsSet.add(POS)
    print tagsSet
    print len(tagsSet)

def print_num_of_different_words():
    sentence_tags = file2sentences(GOLDFILE)
    wordsSet = set()
    for words, tags in sentence_tags:
        for word in words:
            wordsSet.add(word)
    print len(wordsSet)

if __name__ == "__main__":
    main()




