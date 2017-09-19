from __future__ import unicode_literals
import sys, getopt
sys.path.append('../jieba')
sys.path.append('../TextRank4ZH')
import jieba
import textrank4zh

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence


argv=sys.argv[1:]
usage = 'usage: python gen_abstract.py -c <content_filename>'
if len(argv) < 2:
    print(len(argv))
    print(usage)
    sys.exit()
try:
    opts, args = getopt.getopt(argv,"hc:",
        ["content_filename="])
except getopt.GetoptError:
    print(usage)
    sys.exit(2)

for opt, arg in opts:   # parsing arguments
    if opt == '-h':
        print(usage)
        sys.exit()
    elif opt in ("-c", "--content_filename"):
        content_filename = arg

text = open(content_filename, 'r', encoding='utf-8').read()
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)   


tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')

print('\n\n')
print('摘要：')
print('--------------------------------------')
for item in tr4s.get_key_sentences(num=3):
    print(item.index, item.weight, item.sentence)