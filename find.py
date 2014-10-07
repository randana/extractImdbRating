import urllib2
import re

page = urllib2.urlopen('http://www.imdb.com/title/tt0109830/').read()

start_link = page.find('<span itemprop="ratingValue"')
start = page.find('>', start_link+1)
end   = page.find('</span>', start)

rating =  page[start+1 : end]

print rating

#end_quote = page.find (' " ', start + 1)
#matches = re.findall('<span itemprop="ratingValue">', html_content);
#if len(matches) == 0: 
#   print 'I did not find anything'
#else:
#   print 'My string is in the html'
