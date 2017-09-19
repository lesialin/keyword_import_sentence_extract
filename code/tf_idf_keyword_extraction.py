#!/usr/bin/python
#encoding=utf-8
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import sys, getopt
sys.path.append('../jieba')

import jieba
import jieba.posseg
import jieba.analyse
import jieba.posseg as pseg
from operator import itemgetter, attrgetter
    
stopword_path='../jieba/extra_dict/stop_words.txt'
idf_path = '../jieba/extra_dict/idf.txt.big'
dict_path ='../jieba/extra_dict/dict.txt.big'
topK = None
title = ''
content = ''
argv=sys.argv[1:]
usage = 'usage: python tf_idf_keyword_extraction.py -t <title_filename> -c <content_filename> -k <topK>'
if len(argv) < 4:
    print(len(argv))
    print(usage)
    sys.exit()
try:
    opts, args = getopt.getopt(argv,"ht:c:k:",
        ["title_filename=","content_filename=","topK="])
except getopt.GetoptError:
    print(usage)
    sys.exit(2)

for opt, arg in opts:   # parsing arguments
    if opt == '-h':
        print(usage)
        sys.exit()
    elif opt in ("-t", "--title_filename"):
        title_filename = arg
    elif opt in ("-c", "--content_filename"):
        content_filename = arg
    elif opt in ("-k", "--topK"):
        topK = int(arg)

title = open(title_filename, 'r', encoding='utf-8').read()
content = open(content_filename, 'r', encoding='utf-8').read()

words = []

class word:
    x=""   #record keyword
    w=1.0 #tf-idf 
    loc=0 #位置加权
    lenth=1.0 #weight of length
    pos=2.0 #weight of phrase
    def __repr__(self):
            return repr((self.x, self.w, self.loc,self.lenth,self.pos))
    def __init__(self,x,w):
        self.x=x
        self.w=w

# 将新闻标题中的tf-idf值较高的提取出来作为候选关键词,从标题中选择3个
jieba.set_dictionary(dict_path)
jieba.analyse.set_stop_words(stopword_path) 
jieba.analyse.TFIDF(idf_path)
for x,w in jieba.analyse.extract_tags(title,topK=3,withWeight=True):
    words.append(word(x,w))

#将新闻正文中的tf-idf值较高的提取出来作为候选关键词,在这个过程中处理位置加权
for x,w in jieba.analyse.extract_tags(content,withWeight=True):
    ok=0
    i=0
    for i in range(0,words.__len__()):
        if words[i].x==x:
            ok=1
            break
    if ok==1 :
        words[i].loc=1.0
        words[i].w=w
    else:
        words.append(word(x, w))

#计算词长加权
max_len=0
for i in range(0,words.__len__()):
    max_len=max(max_len,len(words[i].x))
for i in range(0,words.__len__()):
    words[i].lenth=float(len(words[i].x))/float(max_len)

#计算词性加权
for i in range(0,words.__len__()):
    temp=pseg.cut(words[i].x)
    for s,flag in temp:
        if flag=='n' :#如果为普通名词
            words[i].pos=1.5
        elif flag[0]=='n' :#如果为专有名词
            words[i].pos=2.0
        elif 'n' in flag :#若为包含名词的词语
            words[i].pos=1.0
        else:
            words[i].pos=0;

#计算总的权值
for i in range(0,words.__len__()):
    words[i].w*=(1+words[i].loc+words[i].lenth+words[i].pos)

#依照最终权值进行排序
words=sorted(words,key=lambda WORD:WORD.w,reverse=True)


#取出前五个作为标签
#print('關鍵字:總權重,位置加權,長度加權,長度加權:)')

print('title:')
print(title)
print('content')
print(content)

print('關鍵字:總權重')
print('--------------------------------------')
for i in range(0,topK):
        #print('%s:(%6.3f,%s,%s,%s)' % (words[i].x,words[i].w,words[i].loc,words[i].lenth,words[i].pos))
        print('%s:%s' %(words[i].x,words[i].w))



