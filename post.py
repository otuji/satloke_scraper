import urllib
import urllib2

url = 'http://satloke.jp/datadetail.php?type=1&id=8355'
values = {'btn_download' : '',
          'x' : '0',
          'y' : '0'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
rep_test = the_page.replace('\r\n','\n')


print the_page.count('\r\n')


f = open("test.che","w")
f.write(rep_test)
f.close()
