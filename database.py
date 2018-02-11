import pymysql

class Database():
    
    def __init__(self):
        # Open database connection
        self.db = pymysql.connect("rapid-814.vm.duke.edu","root","y0ungerisn0w0lder","smart_home_data")

        # prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()
    
    def insertAppliances(self, appliances = []):
        for appliance in appliances:
            sql = "INSERT INTO appliances(timestamp, appliance, energy, power) \
             VALUES (%s, %s, %s, %s)"
            try:
                # Execute the SQL command
                self.cursor.execute(sql, (appliance['timestamp'], appliance['source'], appliance['energy'], appliance['power']))
                # Commit your changes in the database
                self.db.commit()
            except (pymysql.Error, pymysql.Warning) as e:
                # Rollback in case there is any error
                self.db.rollback()
                print('MySQL Error: ' + str(e))
                
    def insertUtilities(self, utilities = []):
        for utility in utilities:
            sql = "INSERT INTO utilities(timestamp, source, energy, power) \
             VALUES (%s, %s, %s, %s)"
            try:
                # Execute the SQL command
                self.cursor.execute(sql, (utility['timestamp'], utility['source'], utility['energy'], utility['power']))
                # Commit your changes in the database
                self.db.commit()
            except (pymysql.Error, pymysql.Warning) as e:
                # Rollback in case there is any error
                self.db.rollback()
                print('MySQL Error: ' + str(e))

        
        

        
