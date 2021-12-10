from dns.resolver import query
import mysql.connector as connector
import time
import cv2
import numpy as np
from PIL import Image as im
import pandas as pd

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
            user='root',
            password='jesus10*',
            database='manthan')
    
        query = 'create table if not exists identified(numberPlate varchar(40) primary key, category varchar(40))'
        cur = self.con.cursor()
        cur.execute(query)
        print()
        print("Database For Identification Connected")
        print()
    
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
    
    def info(self, numberPlate):
        query = "select * from data where numberPlate='"+numberPlate+"'"
        self.con.cursor()
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Informations For "+numberPlate)
            print()
            time.sleep(0.2)
            print("Number Plate : ", row[1])
            time.sleep(0.2)
            print("Owner : ", row[2])
            time.sleep(0.2)
            print("Region : ", row[3])
            time.sleep(0.2)
            print("State : ", row[4])
            time.sleep(0.2)
            print("Vehicle Model : ", row[5])
            print()
            time.sleep(0.2)
            print("Undergone Violations")
            time.sleep(0.2)
            if row[6]=="expired":
                print("Insurance : Expired")
                print("Has To Be Renewed ASAP !")
                print()
            else:
                print("Insurance : Valid")
            time.sleep(0.2)
            if row[7]=="no":
                print("Theft : Not Involved")
            else:
                print("Theft : Involved")
                print("Suspect Vehicle !")
                print()
            time.sleep(0.2)
            if row[8]=="no":
                print("Crime : Not Involved")
                print()
            else:
                print("Crime : Involved")
                print("Suspect Vehicle !")
                print()
            
# Executables
# Identified & Recogonized Number Plates Stored In Array
numbers = ['DL3SAY6324','HR55W4347','DL12SD7561','HR51AA1997','DL01LF7843']
for i in numbers:
    numberPlate = i
    
# Efficient Slicing Of Recogonized Number Plates
    state=numberPlate[:2]
    rto=numberPlate[2:4]
    number=numberPlate[4:]

# Recursively Accessing & Fetching From The Database
    if state=='TN':
        print("Accessing Tamil Nadu State Database...")
        time.sleep(0.8)
        if rto=='07':
            print("Accessing Thiruvanmiyur RTO Database...")
            time.sleep(0.6)
        elif rto=='11':
            print("Accessing Tambaram RTO Database...")
            time.sleep(0.6)
        elif rto=='06':
            print("Accessing Mandavelli RTO Database...")
            time.sleep(0.6)
        elif rto=='23':
            print("Accessing Vellore RTO Database...")
            time.sleep(0.6)
        else:
            print("Accessing RTO's Database...")
            time.sleep(0.6)
            
    elif state=='MH':
        print("Accessing Maharashtra Database...")
        time.sleep(0.8)
        if rto=='05':
            print("Accessing Kalyan RTO Database...")
            time.sleep(0.6)
        elif rto=='25':
            print("Accessing Osmanabad RTO Database...")
            time.sleep(0.6)
        elif rto=='33':
            print("Accessing Gadchiroli RTO Database...")
            time.sleep(0.6)
        elif rto=='51':
            print("Accessing Nashik RTO Database...")
            time.sleep(0.6)
        else:
            print("Accessing RTO's Database...")
            time.sleep(0.6)    
        
    elif state=='KL':
        print("Accessing Kerala Database...")
        time.sleep(0.8)
        if rto=='14':
            print("Accessing Kasargod RTO Database...")
            time.sleep(0.6)
        elif rto=='23':
            print("Accessing Karunagapally RTO Database...")
            time.sleep(0.6)
        elif rto=='65':
            print("Accessing Thirurangadi RTO Database...")
            time.sleep(0.6)
        elif rto=='83':
            print("Accessing Konni RTO Database...")
            time.sleep(0.6)
        else:
            print("Accessing RTO's Database...")
            time.sleep(0.6)
        
    elif state=='KA':
        print("Accessing Karnataka Database...")
        time.sleep(0.8)
        if rto=='03':
            print("Accessing Indiranagar RTO Database...")
            time.sleep(0.6)
        elif rto=='13':
            print("Accessing Hassan RTO Database...")
            time.sleep(0.6)
        elif rto=='19':
            print("Accessing Mangalore RTO Database...")
            time.sleep(0.6)
        elif rto=='28':
            print("Accessing Bijapur RTO Database...")
            time.sleep(0.6)
        else:
            print("Accessing RTO's Database...")
            time.sleep(0.6)
            
    elif state=='DL':
        print("Accessing Delhi Database...")
        time.sleep(0.8)
        if rto=='3S':
            print("Accessing Sheikh Sarai RTO Database...")
            time.sleep(0.6)
        elif rto=='12':
            print("Accessing Vasant Vihar RTO Database...")
            time.sleep(0.6)
        elif rto=='01':
            print("Accessing Mall Road RTO Database...")
            time.sleep(0.6)
        else:
            print("Accessing RTO's Database...")
            time.sleep(0.6)
            
    elif state=='HR':
        print("Accessing Haryana Database...")
        time.sleep(0.8)
        if rto=='51':
            print("Accessing Faridabad RTO Database...")
            time.sleep(0.6)
        elif rto=='55':
            print("Accessing Gurgaon RTO Database...")
            time.sleep(0.6)
        else:
            print("Accessing RTO's Database...")
            time.sleep(0.6)
        
    else:
        print("Accessing State Database...")
        time.sleep(0.8)
        
    helper = DBHelper()
    helper.info(i)

# helper.insert("DL05FJ4923", "Crime")
# helper.fetch("TN22AB7984")