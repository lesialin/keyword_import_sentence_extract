#usage: ./keyword_import_sentence_extract_test.sh
NEWS_DIR=../news_data
#the news duration is from 199102 to 200212
YEARSMONTH=199102
#which news 
#which news 
NO_NEWS_START=40
NO_NEWS_END=45
# print top K keywords
TOPK=3
for((i=NO_NEWS_START;i<=NO_NEWS_END;i++))
do
	NO_NEWS="$((i))"
	./extract_news.sh $NEWS_DIR $YEARSMONTH $NO_NEWS
	python ../code/tf_idf_keyword_extraction.py -t news_title.txt -c news_content.txt -k $TOPK
	python ../code/gen_abstract.py  -c news_content.txt 
done
rm *.txt