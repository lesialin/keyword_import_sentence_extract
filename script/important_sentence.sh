#usage: ./import_sentence.sh 199102 10 
NEWS_DIR=../news_data
#the news duration is from 199102 to 200212
YEARSMONTH=$1
#which news 
NO_NEWS=$2

./extract_news.sh $NEWS_DIR $YEARSMONTH $NO_NEWS
echo 'news content:'
cat news_content.txt

python ../code/gen_abstract.py  -c news_content.txt 

rm *.txt