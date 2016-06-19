# coding: UTF-8

import os
import re
import urllib
import urllib2
from bs4 import BeautifulSoup

values = {'btn_download' : '',
          'x' : '0',
          'y' : '0'}
# for team download
#mode = 'team'
#url = 'http://satloke.jp/datadetail.php?type=1&id='
#last_number = 10023
#last_number = 100

# for match download
#mode = 'match'
#url = 'http://satloke.jp/datadetail.php?type=2&id='
#last_number = 372

# for replay download
mode = 'replay'
url = 'http://satloke.jp/datadetail.php?type=3&id='
last_number = 113

rep = re.compile(r"<[^>]*?>")

os.mkdir(mode)

for id in range(1, last_number+1):

	html = urllib2.urlopen(url+str(id))
	
	soup = BeautifulSoup(html,"lxml")

	td_list = soup.find_all("td", id="data",width="468")

	if len(td_list) == 0:
		print str(id)+"is none!!!!"
		continue

	msg = td_list[0].extract().encode('Shift_JIS')

	file_name = rep.sub("", msg)
	print(file_name)
	
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	binaries = response.read()

	os.mkdir(mode+"\\"+str(id))

	f = open(mode+"\\"+str(id)+"\\"+file_name,"w")
	f.write(binaries)
	f.close()

