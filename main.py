from scrape import EnergyData
from database import Database
import time

energyData = EnergyData()
database = Database()

if __name__ == '__main__': 
    while True:
        database.insertAppliances(energyData.getAppliances())
        database.insertUtilities(energyData.getUtilities())
        time.sleep(5)