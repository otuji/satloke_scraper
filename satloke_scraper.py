# coding: UTF-8

import os
import re
import urllib
import urllib2
from bs4 import BeautifulSoup

values = {'y': '0',
          'x': '0',
          'btn_download': ''}
base_url = 'http://satloke.jp/'


# for team download
mode = 'team'
type = 1
# last_number = 10037
last_number = 1000
header = 'id,file_name,title,introduce,oke_num,control_oke,down_load,data_size,registory_datetime,rating,rating_update_num,rating_update_date\r'


# for match download
# mode = 'match'
#type = 2
# last_number = 372
#header = 'id,file_name,title,introduce,down_load,data_size,registory_datetime\r'


# for replay download
# mode = 'replay'
# type = 3
# last_number = 113
#header = 'id,file_name,title,introduce,down_load,data_size,registory_datetime\r'


rep = re.compile(r"<[^>]*?>")

os.mkdir(mode)

csv = open(mode + "\\team.csv", "w")
csv.write(header)

for id in range(1, last_number + 1):

    html = urllib2.urlopen(base_url + "datadetail.php?type=" + str(type) + "&id=" + str(id))

    soup = BeautifulSoup(html, "lxml")

    td_list = soup.find_all("td", id="data", width="468")

    if len(td_list) == 0:
        print str(id) + "is none!!!!"
        continue

    msg = td_list[0].extract().encode('Shift_JIS')

    file_name = rep.sub("", msg)
    print(file_name)

    # mach or replay 
    if len(td_list) == 6:
        title = rep.sub("", td_list[1].extract().encode('Shift_JIS'))
        introduce = rep.sub("", td_list[2].extract().encode('Shift_JIS'))
        oke_num = 'null'
        control_oke = 'null'
        down_load = rep.sub("", td_list[3].extract().encode('Shift_JIS'))
        file_size = rep.sub("", td_list[4].extract().encode('Shift_JIS'))
        registory_datetime = rep.sub("", td_list[5].extract().encode('Shift_JIS'))
    # team
    else
        title = rep.sub("", td_list[1].extract().encode('Shift_JIS'))
        introduce = rep.sub("", td_list[2].extract().encode('Shift_JIS'))
        oke_num = rep.sub("", td_list[3].extract().encode('Shift_JIS'))
        control_oke = rep.sub("", td_list[4].extract().encode('Shift_JIS'))
        down_load = rep.sub("", td_list[5].extract().encode('Shift_JIS'))
        file_size = rep.sub("", td_list[6].extract().encode('Shift_JIS'))
        registory_datetime = rep.sub("", td_list[7].extract().encode('Shift_JIS'))

    # team rating on
    if len(td_list) == 13:
        rating = rep.sub("", td_list[8].extract().encode('Shift_JIS'))
        rating_update_num = rep.sub("", td_list[9].extract().encode('Shift_JIS'))
        rating_update_date_time = rep.sub("", td_list[10].extract().encode('Shift_JIS'))
    # team rating off or match or replay
    else:
        rating = 'null'
        rating_update_num = 'null'
        rating_update_date_time = 'null'
    
    if len(td_list) == 6:
        csv.write(str(id) + "," + file_name + "," + title + ",\"" + introduce.replace("\r","<br>") + "\"," + oke_num + "," + control_oke + "," + down_load + ",\"" + file_size + "\"," + registory_datetime + ",\"" + rating + "\"," + rating_update_num + "," + rating_update_date_time + "\r")
    else:
        csv.write(str(id) + "," + file_name + "," + title + ",\"" + introduce.replace("\r","<br>") + "\"," + oke_num + "," + control_oke + "," + down_load + ",\"" + file_size + "\"," + registory_datetime + ",\"" + rating + "\"," + rating_update_num + "," + rating_update_date_time + "\r")

    # download *.che file
    data = urllib.urlencode(values)
    req = urllib2.Request(base_url + "datadetail.php?type=" + str(type) + "&id=" + str(id), data)
    response = urllib2.urlopen(req)
    binaries = response.read()

    # save *.che file
    os.mkdir(mode + "\\" + str(id))

    binary_file = open(mode + "\\" + str(id) + "\\" + file_name, "wb")
    binary_file.write(binaries)
    binary_file.close()
    
    # save team emblem file
    req = urllib2.Request(base_url + "draw_emblem.php?type=" + str(type) + "&id=" + str(id) +"&category=team")
    response = urllib2.urlopen(req)
    binaries = response.read()
    emblem_file = open(mode + "\\" + str(id) + "\\emblem_team.png", "wb")
    emblem_file.write(binaries)
    emblem_file.close()
    
    # oke_num 1
    if oke_num == "1":
        image_range = 1
    # oke_num 2 or 3
    else:
        image_range = 3
    
    for index in range(0, range_end):
        # emblem oke image
        req = urllib2.Request(base_url + "draw_emblem.php?type=" + str(type) + "&id=" + str(id) +"&index=" + str(index) + "&category=oke")
        response = urllib2.urlopen(req)
        binaries = response.read()
        emblem_file = open(mode + "\\" + str(id) + "\\emblem_oke_" + str(index) + ".png", "wb")
        emblem_file.write(binaries)
        emblem_file.close()

        # oke image
        req = urllib2.Request(base_url + "draw_snapshot.php?type=" + str(type) + "&id=" + str(id) + "&index=" + str(index))
        response = urllib2.urlopen(req)
        images = response.read()
        image_file = open(mode + "\\" + str(id) + "\\oke_" + str(index) + ".png", "wb")
        image_file.write(images)
        image_file.close()


csv.close()
