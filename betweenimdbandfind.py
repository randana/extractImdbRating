import urllib2
import sys
p1 = sys.argv[1]
p2 = sys.argv[2]

for line in $(cat $p2/movielist.txt); do echo "$line" ;
search_url="http://www.imdb.com/find?ref_=nv_sr_fn&q=$line&s=all"
done;


page = urllib2.urlopen(p1).read()

start_link = page.find('<td class="result_text">')
near_link = page.find("<a href=",start_link+1)
start = page.find('"', near_link+1)
end   = page.find('"', start+1)

title =  page[start+1 : end]

#print title
p1 ="http://www.imdb.com"
#print p1+title
url =p1+title
print url
page = urllib2.urlopen(url).read()

start_link = page.find('<span itemprop="ratingValue"')
start = page.find('>', start_link+1)
end   = page.find('</span>', start)

rating =  page[start+1 : end]

print "Rating:"+rating


