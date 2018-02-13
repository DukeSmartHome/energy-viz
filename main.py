from scrape import EnergyData
from database import Database
import time

energyData = EnergyData()
database = Database()

if __name__ == '__main__':
    while True:
        try:
            database.insertAppliances(energyData.getAppliances())
            database.insertUtilities(energyData.getUtilities())
            print("active")
        except:
            print("error")

        time.sleep(300)
