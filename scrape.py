import requests
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps, loads

class EnergyData:
    appliances = [
    "http://152.3.3.210/cgi-bin/egauge?noteam",
    "http://152.3.3.214/cgi-bin/egauge?noteam",
    "http://152.3.3.235/cgi-bin/egauge?noteam",
    "http://152.3.3.213/cgi-bin/egauge?noteam"]
    utilities = ["http://152.3.3.246/cgi-bin/egauge?noteam",
    "http://152.3.3.236/cgi-bin/egauge?noteam"]

    def getUtilities(self):
        return self.getInfo(self.utilities)

    def getAppliances(self):
        return self.getInfo(self.appliances)

    def getInfo(self, urls):
        rt = []
        for i in urls: #
            r = requests.get(i) # r is a request object
            d = loads(dumps(bf.data(fromstring(r.text)), indent = 4)) # r.text is the xml, bf.data returns OrderedDicts, load+dumps converts to Dict
            timestamp = d["measurements"]["timestamp"]["$"]
            for i in d["measurements"]["meter"]:
                # print("{:<40} {:<20} {:<20}".format(i["@title"],i["energyWs"]["$"],i["power"]["$"]))
                rt.append({"timestamp":timestamp, "source":i["@title"], "energy":i["energyWs"]["$"],"power":i["power"]["$"] })
        return rt

a = EnergyData()
print(a.getUtilities())
print()
print(a.getAppliances())
