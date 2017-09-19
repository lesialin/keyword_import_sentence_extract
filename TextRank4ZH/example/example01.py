#-*- encoding:utf-8 -*-
from __future__ import print_function

import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

text = codecs.open('../test/doc/01.txt', 'r', 'utf-8').read()
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)  

print( '摘要：' )
for item in tr4s.get_key_sentences(num=3):
    print(item.index, item.weight, item.sentence)