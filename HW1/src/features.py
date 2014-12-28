import numpy as np
from tags import TAGS,UglyTAGS

def f1(t_2, t_1, sentence, i, t):
    if sentence[i].endswith("ing") and t == "VBD":
        return 1
    return 0


def f2(t_2, t_1, sentence, i, t):
    if sentence[i].endswith("ed") and t == "VBN":
        return 1
    return 0


def f3(t_2, t_1, sentence, i, t):
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



# def f9(t_2, t_1, sentence, i, t):
#     #Ugly features - meaning all the tags "," ."
#     if t in UglyTAGS:
#         return 1
#     return 0


def combinationtFeature(t_2, t_1, sentence, i, t):
    ret = []
    for t2 in TAGS:
        for t1 in TAGS:
            if t2 == t_2 and t1 == t_1:
                ret.append(1)
            else:
                ret.append(0)
    return ret


#EXPERT_KNOWLEDGE

def expert_knowledge(t_2, t_1, sentence, i, t):
    ek = [e_k_1, e_k_2, e_k_3, e_k_4, e_k_5, e_k_6, e_k_7, e_k_8]
    return [f(t_2, t_1, sentence, i, t) for f in ek]

def e_k_1(t_2, t_1, sentence, i, t):
    try:
        if sentence[i-2] == "of" and sentence[i-1] == "the" and t == "NN":
            return 1
        return 0
    except:
        return 0


def e_k_2(t_2, t_1, sentence, i, t):
    #prob 0.657
    try:
        if sentence[i-2] == "said" and sentence[i-1] == "the" and t == "NN":
            return 1
        return 0
    except:
        return 0


def e_k_3(t_2, t_1, sentence, i, t):
    #prob 0.513
    try:
        if sentence[i-2] == "to" and sentence[i-1] == "be" and t == "VBN":
            return 1
        return 0
    except:
        return 0

def e_k_4(t_2, t_1, sentence, i, t):
    #prob: 0.402
    try:
        if sentence[i-2] == "%" and sentence[i-1] == "of" and t == "DT":
            return 1
        return 0
    except:
        return 0


def e_k_5(t_2, t_1, sentence, i, t):
    #prob: 0.640
    try:
        if sentence[i-2] == "more" and sentence[i-1] == "than" and t == "CD":
            return 1
        return 0
    except:
        return 0


def e_k_6(t_2, t_1, sentence, i, t):
    #prob: 0.965
    try:
        if sentence[i-2] == "did" and sentence[i-1] == "n't" and t == "VB":
            return 1
        return 0
    except:
        return 0

def e_k_7(t_2, t_1, sentence, i, t):
    #prob: 0.603
    try:
        if sentence[i-2] == "the" and sentence[i-1] == "first" and t == "NN":
            return 1
        return 0
    except:
        return 0


def e_k_8(t_2, t_1, sentence, i, t):
    #prob: 0.500
    try:
        if sentence[i-2] == "is" and sentence[i-1] == "a" and t == "JJ":
            return 1
        return 0
    except:
        return 0
###

def F(t_2, t_1, sentence, i, t):
    fs = [f1, f2, f3]
    return np.array([f(t_2, t_1, sentence, i, t) for f in fs] + prevTagFeature(t_2, t_1, sentence, i, t) + prevTagsFeature(t_2, t_1, sentence, i, t) + combinationtFeature(t_2, t_1, sentence, i, t) + expert_knowledge(t_2, t_1, sentence, i, t))

#Returns a feature of size TAGS with 1 at the tag of t_1
def prevTagFeature(t_2, t_1, sentence, i, t):
    res = [0]*len(TAGS)
    if t_1 == "*":
        return res
    try:
        res[TAGS.index(t_1)] = 1
    except:
        pass
    return res

#Returns a feature of size TAGS*TAGS with 1 at the tag of t_1 and t_2
def prevTagsFeature(t_2, t_1, sentence, i, t):
    return prevTagFeature(t_2, t_2, sentence, i, t)+prevTagFeature(t_2, t_2, sentence, i, t)

#Testing
def main():
    history = 'DT', 'NN', 'The dog jumps dog jumps', 2
   # ugly = f9(history,',')
   # print ugly
   # ugly = f9(history,'$')
   # print ugly
   # perv = prevTagFeature(history,'$')
    #print perv
    #pervs = prevTagsFeature(history,'$')
    #print pervs
    pervs = F('DT', 'NN', 'The dog jumps dog jumps', 2, '$')
    print pervs



if __name__ == "__main__":
    main()





