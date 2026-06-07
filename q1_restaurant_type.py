"""
=================================================
ZOMATO DATA ANALYSIS PROJECT
Question 1: Restaurant Type Distribution
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

# Analysis
sns.countplot(x=dataframe['listed_in(type)'])

# Visualization
plt.xlabel("Type of Restaurant")
plt.title("Restaurant Type Distribution")
plt.xticks(rotation=45)
plt.show()

# Conclusion:
# Majority of restaurants fall in the Dining category.