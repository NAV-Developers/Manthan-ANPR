from dns.resolver import query
import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
            user='root',
            password='jesus10*',
            database='manthan')
    
        query = 'create table if not exists identified(numberPlate varchar(40) primary key, category varchar(40))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Table For Identification Created")
    
    # Insert    
    def insert(self, numberPlate, category):
        query = "insert into identified values('{}', '{}')".format(numberPlate, category)
        cur = self.con.cursor()
        cur.execute(query)
        cur.close()
        self.con.commit()
        print("Identified Number Plate Has Been Saved To The Manthan DB")
        
    def fetch(self, numberPlate):
        query = "select * from identified where numberPlate='"+numberPlate+"'"
        self.con.cursor()
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Number Plate : ", row[0])
            print("Category : ", row[1])
                
# Executables
helper = DBHelper()
helper.insert("TN22AB7984", "Crime")
helper.fetch("TN22AB7984")