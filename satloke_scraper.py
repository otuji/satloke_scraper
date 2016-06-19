# coding: UTF-8

import re
import urllib2
from bs4 import BeautifulSoup


html = urllib2.urlopen("http://satloke.jp/datadetail.php?type=1&id=10023")

soup = BeautifulSoup(html,"lxml")

td_list = soup.find_all("td", id="data",width="468")

for td in td_list:
	msg = td.extract().encode('Shift_JIS')
	print(msg)
