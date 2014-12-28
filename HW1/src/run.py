from log_linear import run_fmin_l_bfgs_b
from utils import file2sentences
from viterbi import viterbiAlgo
from features import F
import random
import os
import logging
from time import gmtime, strftime
import string
randomLetters = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.FileHandler("z_log_flow" + randomLetters + ".log", mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
#logging.basicConfig(level=logging.DEBUG, filename=log, filemode='w')
_logger = logging.getLogger("run")
_logger.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(fh)
#_logger.addHandler(fh)


def trainfile():
    src = os.path.dirname(os.path.realpath(__file__))
    HW1 = os.path.dirname(src)
    GOLDFILE = os.path.join(HW1, "data_clean", "sec2-21_first_5000_pos.txt")
    return GOLDFILE


def testfile():
    src = os.path.dirname(os.path.realpath(__file__))
    HW1 = os.path.dirname(src)
    TESTFILE = os.path.join(HW1, "data_clean", "sec2-21_second_5000_pos.txt")
    return TESTFILE


def testtemp():
    src = os.path.dirname(os.path.realpath(__file__))
    HW1 = os.path.dirname(src)
    TESTFILE = os.path.join(HW1, "data_clean", "test_sample.txt")
    return TESTFILE


def traintemp():
    src = os.path.dirname(os.path.realpath(__file__))
    HW1 = os.path.dirname(src)
    TESTFILE = os.path.join(HW1, "data_clean", "train_sample.txt")
    return TESTFILE


def getOutput():
    src = os.path.dirname(os.path.realpath(__file__))
    HW1 = os.path.dirname(src)
    OUT = os.path.join(HW1, "output", "output.txt")
    return OUT


def run():
    sentence_tags = file2sentences(trainfile())
    sentences_counter = 0
    words_counter = 0
    for s, t in sentence_tags:
        sentences_counter += 1
        words_counter += len(s)
    _logger.info("{0} sentences, and {1} words".format(sentences_counter, words_counter))
    _logger.info("Running run_fmin_l_bfgs_b")
    opt = run_fmin_l_bfgs_b(sentence_tags)
    _logger.info("Finish run_fmin_l_bfgs_b")
    v = opt[0]
    src = os.path.dirname(os.path.realpath(__file__))
    HW1 = os.path.dirname(src)
    suffix = "results" + strftime("_%Y_%m_%d_%H_%M_%S") + ".txt"
    outfile = os.path.join(HW1, "output", suffix)
    out = open(outfile, 'a')
    for vv in v:
        out.write(str(vv) + " ")
    out.write("\n")
    out.close()
    test_sentence_tags = file2sentences(testfile())
    new_sentence_tags = []
    for sentence, tags in test_sentence_tags:
        predicted = viterbiAlgo(sentence, v)
        out = open(outfile, 'a')
        if len(predicted) != len(sentence):
            _logger.error("Check your predictor. you have {0} words and {1} predicted tags"
                            .format(len(sentence), len(predicted)))
        for given_tag, word, predicted_tag in zip(tags, sentence, predicted):
            out.write("{0} {1} {2}\n".format(given_tag, word, predicted_tag))
        out.write("\n")
        out.close()
        new_sentence_tags.append((tags, sentence, predicted))

    correct = 0
    total = 0

    for given_tags, words, predicted_tags in new_sentence_tags:
        for given_tag, word, predicted_tag in zip(given_tags, words, predicted_tags):
            total += 1
            if given_tag == predicted_tag:
                correct += 1

    print "total = {0}".format(total)
    print "correct = {0}".format(correct)
    precision = float(correct)/total

    out = open(outfile, 'a')
    out.write("Results:\n")
    out.write("total = {0}, correct = {1}, precision = {2}/n/n".format(total, correct, precision))
    out.write("output:\n")


def infrence(v=None):
    if not v:
        pervs = F('DT', 'NN', 'The dog jumps dog jumps', 2, '$')
        v = [random.random() for _ in range(0, len(pervs))]
    src = os.path.dirname(os.path.realpath(__file__))
    HW1 = os.path.dirname(src)
    suffix = "results" + strftime("_%Y_%m_%d_%H_%M_%S") + ".txt"
    outfile = os.path.join(HW1, "output", suffix)
    out = open(outfile, 'a')
    out.write(str(v))
    out.write("\n")
    out.close()
    test_sentence_tags = file2sentences(testfile())
    new_sentence_tags = []
    for sentence, tags in test_sentence_tags:
        predicted = viterbiAlgo(sentence, v)
        out = open(outfile, 'a')
        if len(predicted) != len(sentence):
            _logger.error("Check your predictor. you have {0} words and {1} predicted tags"
                            .format(len(sentence), len(predicted)))
        for given_tag, word, predicted_tag in zip(tags, sentence, predicted):
            out.write("{0} {1} {2}\n".format(given_tag, word, predicted_tag))
        out.write("\n")
        out.close()
        new_sentence_tags.append((tags, sentence, predicted))

    correct = 0
    total = 0

    for given_tags, words, predicted_tags in new_sentence_tags:
        for given_tag, word, predicted_tag in zip(given_tags, words, predicted_tags):
            total += 1
            if given_tag == predicted_tag:
                correct += 1

    print "total = {0}".format(total)
    print "correct = {0}".format(correct)
    precision = float(correct)/total

    out = open(outfile, 'a')
    out.write("Results:\n")
    out.write("total = {0}, correct = {1}, precision = {2}/n/n".format(total, correct, precision))
    out.write("output:\n")

def loginfo():
    _logger.info("Start time: {0}".format(strftime("%d/%m/%Y - %H:%M:%S")))
    pervs = F('DT', 'NN', 'The dog jumps dog jumps', 2, '$')
    v = [random.random() for _ in range(0, len(pervs))]
    _logger.info("Number of features: {0}".format(len(v)))

def main():
    loginfo()
    run()
    #infrence()


if __name__ == "__main__":
    main()


