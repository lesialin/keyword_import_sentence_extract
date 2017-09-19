NEWS_DIR=$1
#the news duration is from 199102 to 200212
YEARSMONTH=$2
NO_NEWS=$3
#news filename
NEWS_FILENAME=$NEWS_DIR'/cna'$YEARSMONTH
echo 'Extract news:'$NEWS_FILENAME
#num of news 
lines=`wc -l $NEWS_FILENAME | cut -f1 -d' '`
news_lines="$((NO_NEWS*2))"

if [ $news_lines -gt $lines ]; then
	echo 'news no. over the range!'
else
	awk -v l="$((NO_NEWS*2-1))" 'NR==l' $NEWS_FILENAME > news_title.txt
	awk -v l="$((NO_NEWS*2))" 'NR==l' $NEWS_FILENAME > news_content.txt 
	#echo 'news title:'
	#cat news_title.txt
	#echo 'news content:'
	#cat news_content.txt
fi


