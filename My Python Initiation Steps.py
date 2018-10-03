# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:23:41 2018

@author: Jack Chung
"""
# Import these useful packages/modules
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as cp
import seaborn as sns

sns.set()

#==========================================================================
# Working Directory - Change and Check files inside
#**************************************************************************

In [60]: import os
# Check working directory
cwd = os.getcwd()
cwd
# Change working directory (note the style of path \\)
os.chdir('C:\\Users\\user\\Desktop')
# Check the content of working directory (optional)
os.listdir('.')

#============================================================================
# Import .csv from Website as a Pandas dataframe
#****************************************************************************

import pandas as pd
webfile = 'https://.../2008_swing_states.csv' 
df_swing = pd.read_csv(webfile)

import pandas as pd
webfile = 'https://.../2008_swing_states.xlsx' 
df_swing = pd.read_excel(webfile)

#===========================================================================
# Loading a .txt File as a Pandas dataframe
#***************************************************************************

import pandas as pd
file = 'D:\\CUHK MSc Econ...\\Test.txt'
df = pd.read_csv(file, header = None)
df.head()

#============================================================================
# Loading .csv File (Easiest) as a Pandas dataframe
#****************************************************************************

import pandas as pd
filename = 'D:\\CUHK MSc Econ...\\all_medalists.csv'
df = pd.read_csv(filename, sep=';', na_values=".")
df.head()


#============================================================================
# Loading .zip File 
#***************************************************************************

import zipfile
zipfile.ZipFile('D:\\CUHK MSc Econ\\...\\names.zip').extractall('.')

import os
# List the files inside the zip file
os.listdir('.')

# Open a particular file inside the zip file and read the first 10 lines
open('yob2011.txt','r').readlines()[:10]

# Convert one of the .txt files into a pd dataframe
names2011 = pd.read_csv('yob2011.txt',names=['name','sex','number'])
names2011.head()

# Looks like this
       name sex  number
0    Sophia   F   21837
1  Isabella   F   19901
2      Emma   F   18797
3    Olivia   F   17321
4       Ava   F   15496

 
#=============================================================================
# Loading Excel File (Tedious) as a Pandas dataframe, need to change WD first
#*****************************************************************************

import pandas as pd
#  Assign spreadsheet filename to `file` 
file = 'path\\file name.xls'

  e.g.    file = 'C:\\Users....\\TrainExer 2-1.xls'

# Load spreadsheet into the system memory
xl = pd.ExcelFile(file)
# Find Sheet you want by displaying the name, e.g.Dataset Training Exercise 1.3 
print(xl.sheet_names)
['Dataset Training Exercise 1.3']
# Load a sheet into a DataFrame name of your choice
dataframe name = xl.parse('Dataset Training Exercise 1.3')
# Check the Variables
dataframe name.head()

#==============================================================================
# How to get Excel sheet list without opening the Excel file
#*****************************************************************************

# Use the "on_demand = True" flag
xls = pd.ExcelFile('C:\\Users....\\TrainExer 2-1.xls', on_demand = True)
# print out the Excel sheet list
print(xls.sheet_names)

#============================================================================
# Importing files from website to form dataframes using Pandas
#****************************************************************************

import pandas as pd
df = pd.read_csv('https://assets.datacamp.com/production/course_1549/datasets/2008_swing_states.csv')
df.head()
# want to see only few columns and head of the table
df[['col name 1', 'col name 2', 'col name 3']].head()


#=============================================================================
# Loading a Text (.txt) File as a text object
#*****************************************************************************

# If working directory is set up
filename = 'Test.txt' 
# If working directory is not set up, then use 
filename = 'path\\Test.txt'

filename = 'C:\\Users\\user...\\Training Exercises\\Test.txt'
# Apply the open fuction to the file and mode='r' means read only, 
# whereas mode='w' means read and write 
file = open(filename, mode='r')
# Map the text to an object of your choice, say "Text"
Text = file.read()
# Good habit to close the file to avoid overwriting it
file.close
# Look at the text or print it
Text or print(Text)


# A good idea to use Context Manager with to avoid worrying about closing the file 
filename = 'C:\\Users\\user...\\Training Exercises\\Test.txt'
with open(filename, 'r') as file: print(file.read())

#=============================================================================
# Merge multiple data frames into a single data frame for ease of calculation
#*****************************************************************************

# Let’s say we opened a zip file that contained many .txt files of baby neames 
# in years 1880 to 2017. We want to merge them into a single dataframe. 
# So it looks like below. 

'yob1880.txt',
.
.
'yob2016.txt',
'yob2017.txt',

# So let's convert one of them to a pd dataframe and have a look 
names2011 = pd.read_csv('yob2011.txt',names=['name','sex','number'])
names2011.head()

# Now, below are the steps to merge the .txt files into one dataframe:

# Define an empty list ‘each_year' to collect each year data
each_year = []

# Loop over all .txt files from 1880 to 2014 (add 1 to include the last year) 
# to append year numbers from yob****.txt files into each_year[] list. 
# Then add a new column to the end of each dataframe and call it ‘year’. 
# The result is a list of dataframes with headers ‘names’,‘sex’,‘number’,‘year’.

for year in range(1880, 2014+1):
      each_year.append(pd.read_csv('yob{}.txt'.format(year),names=['name','sex','number']))        
      each_year[-1]['year'] = year   

     # This is what we get:  [Dataframe, Dataframe, ..., Dataframe]

# Finally, concatenate every element (dataframe) in the each_year list into a 
# single dataframe called allyears
allyears = pd.concat(each_year)

# Show first five records
allyears.head()

#=============================================================================
# Saving DataFrame from Python to Excel format to PC's working directory
#*****************************************************************************

import pandas as pd
# Aim is to save df in python into Excel format, call it filename
writer = pd.ExcelWriter('filename.xlsx', engine='xlsxwriter')
# Write the dataframe to Excel file
filename.to_excel(writer, 'Sheet1')
# Save it in working directory, and filename.xls will appear in WD
writer.save()

#=============================================================================
#*****************************************************************************
 






