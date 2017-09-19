#usage: ./keyword_extract.sh 199102 10 5
NEWS_DIR=../news_data
#the news duration is from 199102 to 200212
YEARSMONTH=$1
#which news 
NO_NEWS=$2

./extract_news.sh $NEWS_DIR $YEARSMONTH $NO_NEWS
python ../code/gen_abstract.py  -c news_content.txt 

rm *.txt