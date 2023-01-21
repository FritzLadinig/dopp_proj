from ctypes import Array
from sys import displayhook
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


path_CO2_emisions = (r"CO2 emisions/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_4770619.csv")
data_CO2_emisions = pd.read_csv(path_CO2_emisions)

path_CO2_liquid_fuel = (r"CO2 emmisions from liquid CO2/API_EN.ATM.CO2E.LF.KT_DS2_en_csv_v2_4771435.csv")
data_CO2_liquid_fuel = pd.read_csv(path_CO2_liquid_fuel)

plt.rcParams["figure.figsize"] = [15, 7]
plt.rcParams["figure.autolayout"] = True

list_of_countryies = list()
for country_name in data_CO2_emisions["Country Name"]:
    if country_name in data_CO2_liquid_fuel['Country Name'].unique():
        list_of_countryies.append(country_name)



# create figure and axis objects with subplots()
year = list()
for i in range(1960,2023):
   year.append(i)
for country in list_of_countryies:
   fig,ax = plt.subplots()
   # make a plot
   print(data_CO2_liquid_fuel.loc[data_CO2_liquid_fuel['Country Name'] == country].index[0])
   ax.plot(year,
         data_CO2_liquid_fuel.iloc[data_CO2_liquid_fuel.loc[data_CO2_liquid_fuel['Country Name'] == country].index[0],4:],
         color="red", 
         marker="o")
   # set x-axis label
   ax.set_xlabel("year", fontsize = 14)
   # set y-axis label
   ax.set_ylabel("CO@ from liquid",
               color="red",
               fontsize=14)

   # twin object for two different y-axis on the sample plot
   ax2=ax.twinx()
   # make a plot with different y-axis using second axis object
   print(data_CO2_emisions.loc[data_CO2_emisions['Country Name'] == country].index[0])
   ax2.plot(year, data_CO2_emisions.iloc[data_CO2_emisions.loc[data_CO2_emisions['Country Name'] == country].index[0],4:],color="blue",marker="o")
   ax2.set_ylabel("CO2 emmisions total",color="blue",fontsize=14)
   # plt.show()
   # save the plot as a file
   fig.savefig('CO2 overall vs CO2 from liquid fuel/' + country + ".jpeg",
               format='jpeg',
               dpi=100,
               bbox_inches='tight')

