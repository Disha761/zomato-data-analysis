"""
=================================================
ZOMATO DATA ANALYSIS PROJECT
Question 6: Online and Offline Order Analysis
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
pivot_table = dataframe.pivot_table(
    index='listed_in(type)',
    columns='online_order',
    aggfunc='size',
    fill_value=0
)

# Visualization
plt.figure(figsize=(8,6))

sns.heatmap(
    pivot_table,
    annot=True,
    cmap="YlGnBu",
    fmt='d'
)

plt.title("Restaurant Type vs Online Orders")
plt.xlabel("Online Order")
plt.ylabel("Restaurant Type")

plt.show()

# Conclusion:
# Dining restaurants primarily receive offline orders,
# whereas cafes primarily receive online orders.