import urllib2
import re
import sys
p1 = sys.argv[1]
#print p1
page = urllib2.urlopen(p1).read()

start_link = page.find('<span itemprop="ratingValue"')
start = page.find('>', start_link+1)
end   = page.find('</span>', start)

rating =  page[start+1 : end]

print rating


