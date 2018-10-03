# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:08:59 2018

@author: user
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from pandas import plotting
from scipy import stats

#================================================================
#****************************************************************

# Random Number generator
import numpy as np
# Manually seed random number generator if you need reproducibility
np.random.seed(42)
random_numbers = np.random.random(size=10000)

heads = random_numbers < 0.5
print(heads)
np.sum(heads)

#================================================================
#****************************************************************

# Seed the random number generator
np.random.seed(42)

# Initialize random numbers array to store the random numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers), plt.show()

#================================================================
#****************************************************************

# Student’s t-test: 1 sample test using .stats.ttest_1samp()
from scipy import stats
stats.ttest_1samp(data['variable'], meanvalue)

# Student’s t-test: 2 sample test using .stats.ttest_ind():
from scipy import stats

sample_1 = data['variable']
sample_2 = data['variable']

stats.ttest_ind(sample_1, sample_2)




