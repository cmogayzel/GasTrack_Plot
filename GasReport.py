import pandas as pd
import matplotlib.pyplot as plt


#read from CSV file
gasprice = pd.read_csv('FuelTracker_Report.csv', index_col=0)

#Data Subset
fuel_subset = gasprice[["Price","Gallons","GasTotal"]]


#Color scheme list. Red total over $50 and Green = Under $50
colors = []

for lab, rows in fuel_subset.iterrows():
    if rows['GasTotal'] >= 50:
        colors.append('red')
    else:
        colors.append('green')

#inspecting the first 10 values only from the list
colors[:10]

fig = plt.figure(figsize=(12,8))

plt.scatter(fuel_subset.Price,fuel_subset.GasTotal,c=colors)

plt.title("Fuel Cost Tracking")
plt.xlabel("Gas Price")
plt.ylabel("Gas Total")

plt.show()
