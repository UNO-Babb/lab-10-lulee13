#MapPlot.py
#Name:
#Date:
#Assignment:

import energy


energy = energy.get_report()

num_items = len(energy)

years = []
coalProductionData = []

for spot in range (num_items):
    year = energy[spot]["Year"]
    state = energy[spot]["State"]
    coalProduction = int(energy[spot]["Production"]["Coal"])/100
    if state == "Colorado": 
        years.append(year)
        coalProductionData.append(coalProduction)

import matplotlib.pyplot as plt
import numpy as np
plt.plot(years, coalProductionData, 'ro')
plt.ylabel("Coal Production in Trillion BTU")
plt.xlabel("Year")
plt.title("Energy from Coal in Colorado")
plt.savefig("output")