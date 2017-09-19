#usage: ./keyword_extract.sh 199102 10 5
NEWS_DIR=../news_data
#the news duration is from 199102 to 200212
YEARSMONTH=$1
#which news 
NO_NEWS=$2
# print top K keywords
TOPK=$3
./extract_news.sh $NEWS_DIR $YEARSMONTH $NO_NEWS
python ../code/tf_idf_keyword_extraction.py -t news_title.txt -c news_content.txt -k $TOPK
rm *.txt