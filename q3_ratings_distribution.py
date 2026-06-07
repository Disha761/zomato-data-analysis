"""
=================================================
ZOMATO DATA ANALYSIS PROJECT
Question 3: Ratings Distribution
Author: Djoshi
=================================================
"""

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
dataframe = pd.read_csv("Zomato_data.csv")

# Data Cleaning
def handlerate(value):
    value = str(value).split('/')
    return float(value[0])

dataframe['rate'] = dataframe['rate'].apply(handlerate)

# Visualization
plt.hist(dataframe['rate'], bins=5)

plt.title("Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")
plt.show()

# Conclusion:
# Most restaurants receive ratings between 3.5 and 4.