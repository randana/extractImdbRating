import urllib2
import sys
import xlsxwriter

p1 = sys.argv[1]
#print p1
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




def foo():
    print "Counter is %d" % foo.row
foo.row = 0



# Create a workbook and add a worksheet.
#foo();
if foo.row==0:
	workbook = xlsxwriter.Workbook('MovieDatabase.xlsx')
	worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
# Start from the first cell. Rows and columns are zero indexed.

# Iterate over the data and write it out row by row.
worksheet.write(foo.row, 0, "Movie RAting"   )
worksheet.write(foo.row, 1, rating)
foo.row += 1
print foo.row
# Write a total using a formula.

workbook.close()
