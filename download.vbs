Dim ie 
Set ie = CreateObject("InternetExplorer.Application")
ie.Visible = True



ie.Navigate "http://satloke.jp/datadetail.php?type=1&id=10023"
Do While ie.Busy = True Or ie.readyState <> 4
Loop

Dim elms
elms = ie.document.getElementsByTagName(form)



WScript.Sleep(5 * 1000)

ie.Quit
Set ie = Nothing