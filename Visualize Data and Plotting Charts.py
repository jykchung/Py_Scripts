# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:30:41 2018

@author: Jack Chung
"""
#Import these useful packages/modules
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from pandas import plotting





# Visualizing Data
# Use the "Seaborn" visualization format
import seaborn as sns
sns.set()
# Import the Data Exploratory Module "matplotlib"
import matplotlib.pyplot as plt

#================================================================
#****************************************************************

# A user defined function " plt_resize_text" to change title and label font size

def plt_resize_text(labelsize, titlesize):
    ax = plt.subplot()
    for ticklabel in (ax.get_xticklabels()):
        ticklabel.set_fontsize(labelsize)
    for ticklabel in (ax.get_yticklabels()):
            ticklabel.set_fontsize(labelsize)
    ax.xaxis.get_label().set_fontsize(labelsize)
    ax.yaxis.get_label().set_fontsize(labelsize)
    ax.title.set_fontsize(titlesize)

# Then simply insert this function into the code for plotting any chart, e.g.
_=sns.boxplot(x='state', y='dem_share', data=df_swing), plt.xlabel('state'), 
plt.ylabel('percent of vote for Obama'), plt.title('Box Plot'), 
plt_resize_text(20, 40), plt.show()

_ = plt.scatter(df_swing['total_votes'],df_swing['dem_votes'], c='R'), 
plt.xlabel('% of total votes'), plt.ylabel('% votes to Obama'), 
plt.title('Scatter Graph of Votes'), plt_resize_text(20, 40), plt.show()

# Change colour of marker to Red=R, Blue=B, Green=G
_ = plt.scatter(df_swing['total_votes'], df_swing['dem_votes'], c='R'or'B'or'G')

# Set Margin for each plot so the chart is some distance from the axises
plt.margins(0.02)

#================================================================
#****************************************************************

# Bee Swamp Plot
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file "2008_swing_states" as dataframe df_swing
Follow the load file instructions in the intiation.py file

# Set up the swamp plot
_ = sns.swarmplot(x='state', y='dem_share', data=df_swing), plt.xlabel('state')
, plt.ylabel('% of votes for Obama'), plt.title('Swamp Plot'), plt.show()


#================================================================
#****************************************************************

# Histogram (import matplotlib.pyplot as plt)
# The _ is a dummy variable so it won’t show the array
# plt.hist is the function
# bins is the number of intervals for the X variable
_ = plt.hist(df name['variable name'], bins=20), plt.ylabel('name'), plt.xlabel
('name'), plt.title('Swamp Plot'), plt.show()

#================================================================
#****************************************************************

# Cumnulaive Distribution Function (CDF)
# Use the '2008_swing_states.csv" as dataframe "df_swing"
# The x-axis is the sorted data, so we need to generate it using the numpy function “sort”
x = np.sort(df_swing['dem_share'])
# The y-axis is evenly spaced data points between 0 and 1 
y = np.arange(1,len(x)+1)/len(x)
_ = plt.plot(x,y, marker='.', linestyle='none'), plt.ylabel('CDF'), plt.xlabel
('% votes for Obama'), plt.title('Title'), plt.margins(0.02), plt.show()


#================================================================
#****************************************************************

# Scatter Plot
# Import Seaborn for visualization, Matplotlib for plotting
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
# Plot scatter plot using variables in dataframe “df_swing” 
_ = plt.scatter(df_swing['total_votes'], df_swing['dem_votes']), 
plt.ylabel('name'), plt.xlabel('name'), plt.title('Title'), plt.margins(0.02), 
plt.show()
# Change colour of marker to Red=R, Blue=B, Green=G
_ = plt.scatter(df_swing['total_votes'], df_swing['dem_votes'], c='R'or'B'or'G')

#================================================================
#****************************************************************

# Line Plot
# Import Seaborn for visualization, Matplotlib for plotting
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
# Plot Line plot using variables in dataframe “df_swing” 
_ = plt.plot(df_swing['total_votes'], df_swing['dem_votes']), plt.ylabel
('name'), plt.xlabel('name'), plt.title('Title'), plt.margins(0.02), plt.show()

