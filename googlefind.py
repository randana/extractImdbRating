import urllib2
import re

page = urllib2.urlopen('https://www.google.com/search?q=forrest+gump+imdb+rating&gws_rd=ssl').read()

start_link = page.find('Rating')
start = page.find(':', start_link+1)
end   = page.find('/10', start)

rating =  page[start+1 : end]

print rating
