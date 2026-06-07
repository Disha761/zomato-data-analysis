"""
=================================================
ZOMATO DATA ANALYSIS PROJECT
Question 2: Votes Analysis
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
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()

# Visualization
plt.figure(figsize=(8,5))
plt.plot(grouped_data.index, grouped_data.values,
         color='green', marker='o')

plt.xlabel("Restaurant Type")
plt.ylabel("Total Votes")
plt.title("Votes Received by Restaurant Type")
plt.xticks(rotation=45)
plt.show()

# Conclusion:
# Dining restaurants received the maximum votes.