import numpy as np

def f1(history, t):
    t_2, t_1, sentence, i = history
    if sentence[i].endswith("ing") and t == "VBD":
        return 1
    return 0


def f2(history, t):
    t_2, t_1, sentence, i = history
    if sentence[i].endswith("ed") and t == "VBN":
        return 1
    return 0


def f3(history, t):
    t_2, t_1, sentence, i = history
    if sentence[i].endswith("ly") and t == "RB":
        return 1
    return 0

#from tutorial 5 page 10:
#UNIMPLEMENT, WHICH TAG IS EQUIVALENT TO Vt (transitive verb) ?!
def f4(history, t):
    pass

def f5(history, t):
    pass

def f6(history, t):
    pass

def f7(history, t):
    pass

def f8(history, t):
    pass
#until here

#Ugly features
def f9(history, t):
    pass

def F(history, t):
    fs = [f1, f2, f3]
    return np.array([f(history, t) for f in fs])

#Returns a feature of size TAGS with 1 at the tag of t_1
def prevTagFeature():
    return []

#Returns a feature of size TAGS*TAGS with 1 at the tag of t_1 and t_2
def prevTagsFeature():
    return []