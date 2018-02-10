import requests, xmljson
urls = ["http://152.3.3.246/cgi-bin/egauge?noteam",
"http://152.3.3.236/cgi-bin/egauge?noteam",
"http://152.3.3.210/cgi-bin/egauge?noteam",
"http://152.3.3.214/cgi-bin/egauge?noteam",
"http://152.3.3.235/cgi-bin/egauge?noteam",
"http://152.3.3.213/cgi-bin/egauge?noteam"]

for i in urls:
    r = requests.get(i)
    print(r.text)
