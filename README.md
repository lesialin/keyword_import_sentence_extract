### 新聞關鍵字與摘要提取

從新聞標題/內文提取該新聞的摘要及關鍵字



關鍵字提取方法：

TF-IDF

使用jieba套件內的tf-idf功能擷取關鍵字[1]，並且加上位置/關鍵字長度/詞性的加權[2]來計算關鍵字的權重。

TF-IDF（Term Frequency - Inverse Document Frequency )

當一個詞在











摘要提取方法：

TextRank





**使用說明：**

進入script資料夾進行操作

```
cd script/
```

**關鍵字提取**

提取某一則新聞關鍵字

```
#提取cna199102，第10則新聞的五個重要關鍵字
#news資料夾位置設定於該sh檔案中，目前設定路徑為../news_data
./keyword_extract.sh 199102 10 5
```

提取n則新聞關鍵字

```
#提取cna1999102，第40-45則新聞的各三個重要關鍵字 
＃設定sh檔案中YEARMONTH=199102,NO_NEWS_START=40,NO_NEWS_END=45
./keyword_extract_test.sh
```

***重要句子/摘要***

提取某一則新聞重要句子/摘要

```
#提取cna199102，第600則新聞的重要句子/摘要
./import_sentence.sh 199102 600 
```

***關鍵字/摘要提取***

提取某一則新聞關鍵字及摘要(重要句子)

```
#提取cna199102，第20則新聞的5個關鍵字以及重要句子
./keyword_import_sentence_extract.sh 199102 20 5
```

提取n則新聞關鍵字及摘要(重要句子)

```
#提取cna199102，第40-45則新聞的關鍵字及重要句子
./keyword_import_sentence_extract_test.sh
```



***Reference:***

[1] 结巴中文分词:https://github.com/fxsjy/jieba

[2]针对新闻标签提取的tf-idf优化算法1.0版本——基于jieba分词实现:http://www.bijishequ.com/detail/391442?p=56-51-65

[3] 从中文文本中自动提取关键词和摘要:https://github.com/letiantian/TextRank4ZH





