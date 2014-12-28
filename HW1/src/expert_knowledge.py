import utils
import run



def print_tag_followed_pair(pair,num):
    table = {}
    sentence_tags = utils.file2sentences(run.trainfile())
    for s,t in sentence_tags:
        ss = [(s[i-1],s[i]) for i in range(1,len(s))]
        ttt= [(t[i-2],t[i-1],t[i]) for i in range(2,len(s))]
        for t,n_pair in zip(ttt,ss):
            str_pair = " ".join((n_pair))
            if str_pair == pair:
                if t[2] not in table:
                    table[t[2]] = 0
                table[t[2]] += 1
    for key in table:
        table[key] = "{0:.3f}".format(float(table[key])/num)
    print table



table = {}

sentence_tags = utils.file2sentences(run.trainfile())

#table of key: "word word", val: count

k = 0
for s,t in sentence_tags:
    k += 1
    ss = [(s[i-1],s[i]) for i in range(1,len(s))]
    for pair in ss:
        str_pair = " ".join((pair))
        if str_pair not in table:
            table[str_pair] = 0
        table[str_pair] += 1


s_table = sorted(table, key=lambda x: table[x], reverse=True)

for pair in s_table:
    if table[pair] < 100:
        break
    print pair
    print table[pair]
    print_tag_followed_pair(pair,table[pair])
    print "\n\n"




