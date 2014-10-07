import os
from threading import Thread
import sys
import time

pwd = sys.argv[1]


def fetchRating(movie):
	search_url="http://www.imdb.com/find?ref_=nv_sr_fn&q="+movie+"&s=all"	
	print search_url
	print pwd
	file_path = pwd + "/../fetchRating.py search_url movie"
	os.system(file_path);
	return

movies = [line.strip() for line in open(pwd +"/../data/movielist.txt")]

for movie in movies:
#call python file in service to fetch search url
	try:
		t = Thread(target=fetchRating, args=(movie,))
		t.start()
	except:
		print "Error: unable to start thread"		
