## 新聞關鍵字與摘要提取

從新聞標題/內文提取該新聞的摘要及關鍵字

#### 關鍵字提取方法

TF-IDF

使用jieba套件內的tf-idf功能擷取關鍵字[1]，並且加上位置/關鍵字長度/詞性的加權[2]來計算關鍵字的權重。

- TF-IDF（Term Frequency - Inverse Document Frequency )

  當一個詞在這篇文章出現的頻率高，在其他文章內出現的頻率低，這個詞很有可能為這篇文章的關鍵字。TF-IDF演算法包含了兩個部部份：TF詞頻(Term Frequency)以及IDF逆向文件頻率(Inverse Document Frequency)。

  $tf_{t,d}$表示在_t_詞在文件_d_中t出現的頻率，$idf_t=log(\frac{D}{d_t})$ 表示在_t_詞在D個文件中出現的頻率。一個詞_t_在文章_d_中關鍵字的權重$w_{t,d}=tf_{t,d}*idf_t$


- 位置加權

  根據詞出現的位置給予較高的權重

  $\begin{cases}w_t^{loc}=1.5 , if 詞出現title\\ w_t^{loc}=0, if 詞出現在內文\end{cases}$


- 詞性加權

  根據名詞的屬性給予不同的權重

  ​$\begin{cases}w_t^{p}=0 , if 非名詞\\ w_t^{lp}=1.5, if 普通名詞\\w_t^{lp}=2, if 專有名詞\\w_t^{lp}=1, if 包含名詞的名詞\end{cases}$

- 長度加權

  ​長度長的詞給予較高的權重

  ​$w_t^l=\frac{len(w_t)}{max(len(w_1),...len(w_k))}$



**關鍵字總權重**

$w_t=tf_{t,d}*idf_t*(1+w_t^{loc}+w_t^p+w_t^l)$

這裡使用[2]來提取關鍵字

#### 摘要提取方法

##### TextRank

TextRank延伸PageRank的概念，計算句子的重要。

步驟如下：

1. 將本文分割成句子$S_1,S_2...,S_m$，以句子為節點建構圖

2. 計算句子的相似度

   $Similarity(S_i,S_j)=\frac{|\{w_k|w_k\in S_i\& w_k \in S_j\}|}{log(|S_i|)+log(|S_j|)}$

3. 句子權重

   $WS(V_i)=(1-d)+d*\displaystyle\sum_{V_j\in In(V_i)}\frac{w_{ji}}{\sum_{V_k\in Out(V_j)}WS(V_j)}$

4. 根據分數抽取重要分數的句子作為摘要

這裡使用[3]套件來提取文章的摘要/重要句。



### 使用說明：
Requirement
```
pip install networkx
```

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



#### 心得：

不管是用TF_IDF或是TextRank的方法來提取關鍵字以及摘要，有很大的關鍵在於斷字的處理，包含停用字以及idf資料文字檔的好壞。目前使用jieba斷句的結果不甚理想。有時間的話應該要試試不用斷字的演算法來處理。
