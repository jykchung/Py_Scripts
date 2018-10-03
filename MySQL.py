# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:35:02 2018

@author: Jack Chung
"""
import pymysql.cursors
import datetime as dt

#================================================================
# Create Database****************************************************

connection = pymysql.connect(host='localhost',
                             user='root',
                             port=3306,
                             password='')
try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE tutorial_database1')
       
finally:
    connection.close()  
#================================================================
# Creating a Table************************************************
    
connection = pymysql.connect(host='localhost',
                             user='root',
                             port=3306,
                             password='',
                             db='tutorial_database1',
                             cursorclass=pymysql.cursors.DictCursor) # use SSCursor for complex problem or slow network   
  
try:
    with connection.cursor() as cursor:
        sqlQuery= "CREATE TABLE IF NOT EXISTS sdata(Date INT, Open DECIMAL(18,4), High DECIMAL(18,4), Low DECIMAL(18,4), Close DECIMAL(18,4), Volume INT)"
        cursor.execute(sqlQuery)
       
finally:
    connection.close() 
    
#================================================================
# Inserting Data into Table**************************************

myDate = dt.datetime(2000,1,1)

connection = pymysql.connect(host='localhost',
                             user='root',
                             port=3306,
                             password='',
                             db='tutorial_database1',
                             cursorclass=pymysql.cursors.DictCursor)    
    
try:
    with connection.cursor() as cursor:
        sqlQuery= "INSERT INTO sdata(`Date`, `Open`, `High`, `Low`, `Close`, `Volume`) VALUES (%s, %s, %s, %s, %s, %s)"  # use ` not ' marks!!!
        cursor.execute(sqlQuery, (myDate, float(10.10), float(10.45), float(10.08), float(10.30), int(250000)))        # Insert specified data  
        connection.commit()   # save changes
finally:
    connection.close()   
    
#================================================================
# Querying Data**************************************************

myDate = dt.datetime(2000,1,1)

connection = pymysql.connect(host='localhost',
                             user='root',
                             port=3306,
                             password='',
                             db='tutorial_database1',
                             cursorclass=pymysql.cursors.DictCursor)    
    
try:
    with connection.cursor() as cursor:
        sqlQuery= "SELECT `Open`, `High` FROM `sdata` WHERE `Volume`>%s"  # use ` not ' marks!!!
        cursor.execute(sqlQuery, ('0'))         
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()      
