# coding: UTF-8

import re
import urllib2
from bs4 import BeautifulSoup

base_url = 'http://satloke.jp/'

# for match download
mode = 'match'
type = 2
header = 'type,id,title,comment,osusume,date,mode,del\r'
id_array = [1, 5, 20, 32, 93, 99, 109, 122, 123, 148, 202]

# for replay download
#mode = 'replay'
#type = 3
#header = 'type,id,title,comment,osusume,date,mode,del\r'
#id_array = [12, 18, 20, 21, 23, 37, 53, 64, 65]

rep = re.compile(r"<[^>]*?>")

csv = open( mode + ".csv", "w")
csv.write(header)

for id in id_array:
    print(str(type) + ":" + str(id))

    html = urllib2.urlopen(base_url + "datadetail.php?type=" + str(type) + "&id=" + str(id))

    soup = BeautifulSoup(html, "lxml")

    comment_table = soup.find_all("table", border="1", width="933")

    tr_array = comment_table.find_all("tr")

    for tr in range(1, len(tr_array)):
        if tr == 0:
            continue
        td_array = rep.sub("", tr_array.find_all("td").extract().encode('Shift_JIS')
        csv.write(td_array[0] + "," + td_array[1] + "," + td_array[2] + "," + td_array[3] + "," + td_array[4] + "," + td_array[5] + "\r")
csv.close()
