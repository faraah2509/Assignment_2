# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:32:42 2023

@author: Syeda Farah Ali
SRN 18055812
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
file_path = 'C:/dataset/Latest Published Global Estimates (1751-2013).xlsx'
data = pd.read_excel(file_path)

print(data.head(5))

# Display summary statistics
print(data.describe())




plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Total'], marker='o')
plt.title('Total over the Years')
plt.xlabel('Year')
plt.ylabel('Total')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(data['Year'], data['Gas'], label='Gas')
plt.bar(data['Year'], data['Liquids'], label='Liquids')
plt.bar(data['Year'], data['Solids'], label='Solids')
plt.title('Gas, Liquids, and Solids over the Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data['Production'], bins=20)
plt.title('Production Distribution')
plt.xlabel('Production')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(data['Production'], data['Flaring'])
plt.title('Production vs Flaring')
plt.xlabel('Production')
plt.ylabel('Flaring')
plt.show()

sum_gas_liquids_solids = data[['Gas', 'Liquids', 'Solids']].sum(axis=1)
plt.figure(figsize=(10, 6))
plt.bar(data['Year'], sum_gas_liquids_solids)
plt.title('Sum of Gas, Liquids, and Solids by Year')
plt.xlabel('Year')
plt.ylabel('Total Amount')
plt.show()

plt.figure(figsize=(10, 6))
plt.stackplot(data['Year'], data['Gas'], data['Liquids'], data['Solids'], labels=['Gas', 'Liquids', 'Solids'])
plt.title('Stacked Area Chart of Gas, Liquids, and Solids over the Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend(loc='upper left')
plt.show()

