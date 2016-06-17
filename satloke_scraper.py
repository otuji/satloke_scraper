# coding: EUC-JP

import urllib2
from bs4 import BeautifulSoup


id = 1023 

html = urllib2.urlopen("http://satloke.jp/datadetail.php?type=1&id=1023")

soup = BeautifulSoup(html)

td_list = soup.find_all("td", id="data")

file_name = td_list[1]

introduction = td_list[3]

oke_num = td_list[5]

download_num = td_list[7]

data_size = td_list[9]

registory_date = td_list[11]

rating = td_list[13]

rating_update_num = td_list[15]

rating_update_date = td_list[17]

team_emblem = td_list[19]


print("%s",td_list)