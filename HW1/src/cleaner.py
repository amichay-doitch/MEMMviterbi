f1 = "C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data\sec2-21_first_5000_pos.txt"
f2 = "C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data\sec2-21_second_5000_pos.txt"
f3 = "C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data\\test_sample.txt"
f4 = "C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data\\train_sample.txt"

target = {
    f1:"C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data_clean\sec2-21_first_5000_pos.txt",
    f2 : "C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data_clean\sec2-21_second_5000_pos.txt",
    f3 : "C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data_clean\\test_sample.txt",
    f4 : "C:\Users\user\Dropbox\NLP\NLPamichayIftah\HW1\data_clean\\train_sample.txt",
}

ALLTAGS = set(['PRP$', 'VBG', 'VBD', 'VBN', ',', "''", 'VBP', 'WDT', 'JJ', 'WP', 'VBZ', 'DT', '#', 'RP', '$', 'NN', 'FW', 'POS', '.', 'TO', 'PRP', 'RB', '-LRB-', ':', 'NNS', 'NNP', '``', 'WRB', 'CC', 'LS', 'PDT', 'RBS', 'RBR', 'CD', '-NONE-', 'EX', 'IN', 'WP$', 'MD', 'NNPS', '-RRB-', 'JJS', 'JJR', 'SYM', 'VB', 'UH'])
UglyTAGS = set([',' , "''" , '#' , '$' , '.' , ':' ,'``', '-LRB-','-RRB-','-NONE-'])
TAGS = set(['PRP$', 'VBG', 'VBD', 'VBN', 'VBP', 'WDT', 'JJ', 'WP', 'VBZ', 'DT', 'RP', 'NN', 'FW', 'POS', 'TO', 'LS','RB', 'NNS', 'PRP', 'VB', 'WRB', 'CC', 'PDT', 'RBS', 'RBR', 'CD', 'EX', 'IN', 'WP$', 'MD', 'NNPS', 'JJS', 'JJR', 'SYM', 'UH', 'NNP'])
tags = set()
for f in [f1,f2,f3,f4]:
    relevant = []
    ff = open(f,'r')
    for line in ff.readlines():
        if line and line.strip():
            t,w = line.strip().split(" ")
            if t not in UglyTAGS:
                relevant.append((t,w))
        else:
            relevant.append((" ", " "))
    fo = target[f]
    fo = open(fo, 'w')
    for t, w in relevant:
        fo.write(" ".join((t, w)))
        fo.write("\n")

