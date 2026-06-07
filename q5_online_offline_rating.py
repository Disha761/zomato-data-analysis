"""
=================================================
ZOMATO DATA ANALYSIS PROJECT
Question 5: Online vs Offline Ratings
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
plt.figure(figsize=(6,6))

sns.boxplot(
    x='online_order',
    y='rate',
    data=dataframe
)

plt.title("Online Order vs Restaurant Ratings")
plt.xlabel("Online Order")
plt.ylabel("Rating")

plt.show()

# Conclusion:
# Offline orders received lower ratings
# compared to online orders.