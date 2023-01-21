from ctypes import Array
from sys import displayhook
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


path_nuclear = (r"Nuclear Energy and alternatives/API_EG.USE.COMM.CL.ZS_DS2_en_csv_v2_4772913.csv")
data_nuclear = pd.read_csv(path_nuclear)

path_exposure = (r"percentage of exposure of CO2/API_EN.ATM.PM25.MC.ZS_DS2_en_csv_v2_4771785.csv")
data_exposure = pd.read_csv(path_exposure)

plt.rcParams["figure.figsize"] = [15, 7]
plt.rcParams["figure.autolayout"] = True

list_of_countryies = list()
for country_name in data_nuclear["Country Name"]:
    if country_name in data_exposure['Country Name'].unique():
        list_of_countryies.append(country_name)



# create figure and axis objects with subplots()
year = list()
for i in range(1960,2023):
   year.append(i)
for country in list_of_countryies:
   fig,ax = plt.subplots()
   # make a plot
   print(data_exposure.loc[data_exposure['Country Name'] == country].index[0])
   ax.plot(year,
         data_exposure.iloc[data_exposure.loc[data_exposure['Country Name'] == country].index[0],4:],
         color="red", 
         marker="o")
   # set x-axis label
   ax.set_xlabel("year", fontsize = 14)
   # set y-axis label
   ax.set_ylabel("exposure percentage CO2",
               color="red",
               fontsize=14)

   # twin object for two different y-axis on the sample plot
   ax2=ax.twinx()
   # make a plot with different y-axis using second axis object
   print(data_nuclear.loc[data_nuclear['Country Name'] == country].index[0])
   ax2.plot(year, data_nuclear.iloc[data_nuclear.loc[data_nuclear['Country Name'] == country].index[0],4:],color="blue",marker="o")
   ax2.set_ylabel("nuclear energy",color="blue",fontsize=14)
   # plt.show()
   # save the plot as a file
   fig.savefig('nuclear energy vs CO2 over-exposure/' + country + ".jpeg",
               format='jpeg',
               dpi=100,
               bbox_inches='tight')

