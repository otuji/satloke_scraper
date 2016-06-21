# coding: UTF-8

import os
import re
import urllib
import urllib2
from bs4 import BeautifulSoup

values = {'y' : '0',
          'x' : '0',
          'btn_download' : ''}
# for team download
mode = 'team'
url = 'http://satloke.jp/datadetail.php?type=1&id='
#last_number = 10023
last_number = 10
header = 'id,file_name,title,introduce,oke_num,control_oke,down_load,data_size,registory_datetime,rating,rating_update_num,rating_update_date\r\n'

# for match download
#mode = 'match'
#url = 'http://satloke.jp/datadetail.php?type=2&id='
#last_number = 372



# for replay download
#mode = 'replay'
#url = 'http://satloke.jp/datadetail.php?type=3&id='
#last_number = 113


rep = re.compile(r"<[^>]*?>")

os.mkdir(mode)

csv = open(mode+"\\team.csv","w")
csv.write(header)


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
	
	title = rep.sub("", td_list[1].extract().encode('Shift_JIS'))
	introduce = rep.sub("", td_list[2].extract().encode('Shift_JIS'))
	oke_num = rep.sub("", td_list[3].extract().encode('Shift_JIS'))
	control_oke = rep.sub("", td_list[4].extract().encode('Shift_JIS'))
	down_load = rep.sub("", td_list[5].extract().encode('Shift_JIS'))
	file_size = rep.sub("", td_list[6].extract().encode('Shift_JIS'))
	registory_datetime = rep.sub("", td_list[7].extract().encode('Shift_JIS'))
	rating = rep.sub("", td_list[8].extract().encode('Shift_JIS'))
	rating_update_num = rep.sub("", td_list[9].extract().encode('Shift_JIS'))
	rating_update_date_time = rep.sub("", td_list[10].extract().encode('Shift_JIS'))
	csv.write(str(id)+","+file_name+","+title+","+introduce+","+oke_num+","+control_oke+","+down_load+","+file_size+","+registory_datetime+","+rating+","+rating_update_num+","+rating_update_date_time+"\r\n")
	
	
	data = urllib.urlencode(values)
	req = urllib2.Request(url+str(id), data)
	response = urllib2.urlopen(req)
	binaries = response.read()

	os.mkdir(mode+"\\"+str(id))

	f = open(mode+"\\"+str(id)+"\\"+file_name,"wb")
	f.write(binaries)
	f.close()


csv.close()
