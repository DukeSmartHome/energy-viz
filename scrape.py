import requests
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps, loads

class EnergyData:

    def __init__(self):
        self.appliances = [
        "http://152.3.3.210/cgi-bin/egauge?noteam",
        "http://152.3.3.214/cgi-bin/egauge?noteam",
        "http://152.3.3.235/cgi-bin/egauge?noteam",
        "http://152.3.3.213/cgi-bin/egauge?noteam"]
        self.utilities = ["http://152.3.3.246/cgi-bin/egauge?noteam",
        "http://152.3.3.236/cgi-bin/egauge?noteam"]
        self.prevUtilities = dict()
        self.prevAppliances = dict()

    def subDict(self,a, b):
        for i in range(len(a)):
            a[i]["energy"] = a[i]["energy"] - b[i]["energy"]
        return a

    def getUtilities(self):
        if any(self.prevUtilities):
            latest = self.getInfo(self.utilities)
            diff = self.subDict(latest, self.prevUtilities)
            return diff
        self.prevUtilities = self.getInfo(self.utilities)
        return dict()

    def getCumulativeUtilities(self):
        return self.getInfo(self.utilities)

    def getCumulativeAppliances(self):
        return self.getInfo(self.appliances)

    def getAppliances(self):
        if any(self.prevAppliances):
            latest = self.getInfo(self.appliances)
            diff = self.subDict(latest, self.prevAppliances)
            return diff
        self.prevAppliances = self.getInfo(self.appliances)
        return dict()

    def getInfo(self, urls):
        rt = []
        for i in urls: #
            try:
                r = requests.get(i) # r is a request object
                d = loads(dumps(bf.data(fromstring(r.text)), indent = 4)) # r.text is the xml, bf.data returns OrderedDicts, load+dumps converts to Dict
                timestamp = d["measurements"]["timestamp"]["$"]
                for i in d["measurements"]["meter"]:
                    # print("{:<40} {:<20} {:<20}".format(i["@title"],i["energyWs"]["$"],i["power"]["$"]))
                    rt.append({"timestamp":timestamp, "source":i["@title"], "energy":i["energyWs"]["$"],"power":i["power"]["$"] })
            except:
                print("network error")

        return rt
