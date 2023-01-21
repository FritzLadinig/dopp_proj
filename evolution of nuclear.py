from ctypes import Array
from sys import displayhook
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


path_nuclear = (r"Nuclear Energy and alternatives/API_EG.USE.COMM.CL.ZS_DS2_en_csv_v2_4772913.csv")
data_nuclear = pd.read_csv(path_nuclear)

path_gdp = (r"DataSets/GDP.csv")
data_gdp = pd.read_csv(path_gdp)

plt.rcParams["figure.figsize"] = [15, 7]
plt.rcParams["figure.autolayout"] = True

list_of_countryies = list()
for country_name in data_nuclear["Country Name"]:
    if country_name in data_gdp['Country Name'].unique():
        list_of_countryies.append(country_name)



# create figure and axis objects with subplots()
year = list()
for i in range(1960,2023):
   year.append(i)
for country in list_of_countryies:
   fig,ax = plt.subplots()
   # make a plot
   print(data_gdp.loc[data_gdp['Country Name'] == country].index[0])
   ax.plot(year,
         data_gdp.iloc[data_gdp.loc[data_gdp['Country Name'] == country].index[0],4:],
         color="red", 
         marker="o")
   # set x-axis label
   ax.set_xlabel("year", fontsize = 14)
   # set y-axis label
   ax.set_ylabel("GDP",
               color="red",
               fontsize=14)

   # twin object for two different y-axis on the sample plot
   ax2=ax.twinx()
   # make a plot with different y-axis using second axis object
   print(data_nuclear.loc[data_nuclear['Country Name'] == country].index[0])
   ax2.plot(year, data_nuclear.iloc[data_nuclear.loc[data_nuclear['Country Name'] == country].index[0],4:],color="blue",marker="o")
   ax2.set_ylabel("Nuclear",color="blue",fontsize=14)
   # plt.show()
   # save the plot as a file
   fig.savefig('GDP vs nuclear for each country/' + country + ".jpeg",
               format='jpeg',
               dpi=100,
               bbox_inches='tight')

