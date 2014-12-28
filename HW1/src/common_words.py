import utils
import run

"""
table = {}
contains
table[word] = {tag:num,
               tag:num,

                        }
"""
def main():
    sum_words = 0
    different_words = set()
    table = {}
    sentence_tags = utils.file2sentences(run.trainfile())
    for sentence, tags in sentence_tags:
        for s, t in zip(sentence, tags):
            different_words.add(s)
            sum_words += 1
            if s not in table:
                table[s] = {}
                table[s][t] = 1
            else:
                if t not in table[s]:
                    table[s][t] = 0
                table[s][t] += 1
    count = 0
    unique = 0
    table_output = {}
    for word in table:
        if len(table[word]) == 1:
            key = table[word].keys()[0]
            if table[word][key] >= 10:
                table_output[word] = key
                unique += table[word][key]
                print word
                print table[word]

                count += 1

                print "\n"
    print count
    print sum_words
    print unique
    print float(unique)/sum_words * 100
    print len(different_words)
    print float(count)/len(different_words)
    print table_output
if __name__ == "__main__":
    main()