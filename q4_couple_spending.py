"""
=================================================
ZOMATO DATA ANALYSIS PROJECT
Question 4: Average Spending of Couples
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
couple_data = dataframe['approx_cost(for two people)']

# Visualization
plt.figure(figsize=(8,5))
sns.countplot(x=couple_data)

plt.title("Approximate Cost for Two People")
plt.xlabel("Cost (INR)")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)

plt.show()

# Conclusion:
# The majority of couples prefer restaurants
# with an approximate cost of 300 rupees.