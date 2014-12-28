import random
import re
from utils import probability
from tags import TAGS, table
import logging
import time
_logger = logging.getLogger("viterbi")
_logger.setLevel(logging.DEBUG)


def q(t_2, t_1, sentence, i, t, V):
    return probability(t_2, t_1, sentence, i, t, V)



def viterbiAlgo(sentence, V):
    _logger.info('Enter to Viterbi with sentence: \n"{0}"'.format(" ".join(sentence)))
    n = len(sentence)
    lenTags = len(TAGS)
    pi = [[[0 for k in xrange(lenTags)] for j in xrange(lenTags)] for i in xrange(n)]
    bp = [[[0 for k in xrange(lenTags)] for j in xrange(lenTags)] for i in xrange(n)]
    #S-1 = S0 = {*} and Sk = S = TAGS - according to HMM-1-video5 on minute 07:23
    for k in xrange(n):
        word = sentence[k]

        print 'k', k
        if k == 0:
            if word in table:
                v1 = TAGS.index(table[word])
                pi[k][0][v1] = 1
                bp[k][0][v1] = table[word]
                continue
            for v0 in xrange(lenTags):
                qq = probability('*', '*', sentence, k, TAGS[v0], V)
                if qq > pi[k][0][v0]:
                    pi[k][0][v0] = qq
                    bp[k][0][v0] = TAGS[v0]

        elif k == 1:
            if word in table:
                v1 = TAGS.index(table[word])
                for u1 in xrange(lenTags):
                    pi[k][u1][v1] = 1
                    bp[k][u1][v1] = table[word]
                continue
            for u1 in xrange(lenTags):
                for v1 in xrange(lenTags):
                    qq = probability('*', TAGS[u1], sentence, k, TAGS[v1], V)
                    if (pi[0][0][u1]*qq) > pi[k][u1][v1]:
                        pi[k][u1][v1] = pi[0][0][u1]*qq
                        bp[k][u1][v1] = TAGS[v1]

        elif k > 1:
            if word in table:
                v1 = TAGS.index(table[word])
                for u1 in xrange(lenTags):
                    pi[k][u1][v1] = 1
                    bp[k][u1][v1] = table[word]
                continue
            for u in xrange(lenTags):
                print 'u', u
                for v in xrange(lenTags):
                    for t in xrange(lenTags):
                        qq = probability(TAGS[t], TAGS[u], sentence, k, TAGS[v], V)
                        if (pi[k-1][t][u]*qq) > pi[k][u][v]:
                            pi[k][u][v] = pi[k-1][t][u]*qq
                            bp[k][u][v] = TAGS[v]
                            #bp[k][u][v] = TAGS[t] - Eyal

    #Get the final tags
    tags = [None]*n
    argmax = 0
    for u in xrange(lenTags):
         for v in xrange(lenTags):
            if pi[n-1][u][v] >= argmax:
                argmax = pi[n-1][u][v]
                tags[n-1] = TAGS[v]
                tags[n-2] = TAGS[u]
    for k in xrange(n-3, -1, -1):
        print k
        print bp
        tags[k] = bp[k+2][TAGS.index(tags[k+1])][TAGS.index(tags[k+2])]
    return tags


def main():
    history = 'DT', 'NN', 'The dog jumps dog jumps', 2
    tags = viterbiAlgo(history[2])
    print tags

if __name__ == "__main__":
    main()
