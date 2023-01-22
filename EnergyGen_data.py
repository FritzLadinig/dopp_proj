import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pathlib

countries=[
    "Canada", "Mexico", "US", "Total North America", 
    "Argentina", "Brazil", "Chile", "Colombia", "Ecuador", "Peru", "Venezuela", "Total S. & Cent. America",
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", 
    "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
    "Iceland", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Netherlands", 
    "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Slovakia", 
    "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom",
    "Other Europe", "Total Europe",
    "Azerbaijan", "Belarus", "Kazakhstan", "Russian Federation", "Turkmenistan", "USSR", 
    "Uzbekistan", "Other CIS", "Total CIS",
    "Iran", "Iraq", "Israel", "Kuwait", "Oman", "Qatar", "Saudi Arabia", "United Arab Emirates",
    "Other Middle East", "Total Middle East", 
    "Algeria", "Egypt", "Morocco", "South Africa", "Eastern Africa", "Middle Africa", "Western Africa",
    "Other Northern Africa", "Other Southern Africa",
    "Australia", "Bangladesh", "China", "China Hong Kong SAR", "India", "Indonesia", "Japan", "Malaysia", 
    "New Zealand", "Pakistan", "Philippines", "Singapore", "South Korea", "Sri Lanka", "Taiwan", "Thailand", 
    "Vietnam", "Total Asia Pacific"

]

def load_oil_gen(filepath):
    df_generation=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Oil Production - Tonnes", header=2)
    df_generation=df_generation.rename(columns={"Million tonnes": "country"})
    
    df_generation=df_generation.set_index("country")
    # print(countries)
    countries_oil = list()
    for i in range(1, 77):
        countries_oil.append(df_generation.index[i])
    # print(countries_oil)
    df_generation=df_generation.loc[countries_oil]
    df_generation=df_generation.fillna(0.0)
    
    return df_generation


def load_oil_cons(filepath):
    df_consumption=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Oil Consumption - Tonnes", header=2)
    df_consumption=df_consumption.rename(columns={"Million tonnes": "country"})
    
    df_consumption=df_consumption.set_index("country")
    # print(countries)
    countries_oil = list()
    for i in range(1, 77):
        countries_oil.append(df_consumption.index[i])
    # print(countries_oil)
    df_consumption=df_consumption.loc[countries_oil]
    df_consumption=df_consumption.fillna(0.0)
    
    return df_consumption



def load_coal_cons(filepath):
    df_consumption=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Coal Consumption - EJ", header=2)
    df_consumption=df_consumption.rename(columns={"Exajoules": "country"})
    
    df_consumption=df_consumption.set_index("country")
    # print(countries)
    countries_oil = list()
    for i in range(1, 77):
        countries_oil.append(df_consumption.index[i])
    # print(countries_oil)
    df_consumption=df_consumption.loc[countries_oil]
    df_consumption=df_consumption.fillna(0.0)
    
    return df_consumption


def load_gas_gen(filepath):
    df_generation=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Gas Production - Bcm", header=2)
    df_generation=df_generation.rename(columns={"Billion cubic metres": "country"})
    
    df_generation=df_generation.set_index("country")
    # print(countries)
    countries_oil = list()
    for i in range(1, 77):
        countries_oil.append(df_generation.index[i])
    # print(countries_oil)
    df_generation=df_generation.loc[countries_oil]
    df_generation=df_generation.fillna(0.0)
    
    return df_generation


def load_gas_cons(filepath):
    df_consumption=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Gas Consumption - Bcm", header=2)
    df_consumption=df_consumption.rename(columns={"Billion cubic metres": "country"})
    
    df_consumption=df_consumption.set_index("country")
    # print(countries)
    countries_oil = list()
    for i in range(1, 77):
        countries_oil.append(df_consumption.index[i])
    # print(countries_oil)
    df_consumption=df_consumption.loc[countries_oil]
    df_consumption=df_consumption.fillna(0.0)
    
    return df_consumption


def load_total_CO2_energy(filepath):
    df_consumption=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="CO2 Emissions from Energy", header=2)
    df_consumption=df_consumption.rename(columns={"Million tonnes of carbon dioxide": "country"})
    
    df_consumption=df_consumption.set_index("country")
    # print(countries)
    countries_oil = list()
    for i in range(1, 77):
        countries_oil.append(df_consumption.index[i])
    # print(countries_oil)
    df_consumption=df_consumption.loc[countries_oil]
    df_consumption=df_consumption.fillna(0.0)
    
    return df_consumption


def for_energy_total():
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    df_consumtion = load_total_CO2_energy(pathToData)
    define_ratio = 1
    # print(df_consumtion.columns[10])
    df2 = df_consumtion.sort_values(2021)
    df2 = df2.drop([np.nan])
    df2 = df2.select_dtypes(exclude=['object', 'datetime']) * define_ratio
    for i in range(0, 65,10):
        df2.iloc[i:i+10,0:55].T.plot()
        
        # plt.title('Million tonnes of CO2 from energy production per country')
        # plt.xlabel('Year')
        # plt.ylabel('Million Tonnes') 
        # plt.autoscale
        # plt.show()
        # plt.savefig("plots CO2 production/plot for countries in list" + str(i) + " " + str(i+10))
    return df2



def for_oil():
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    df_generation=load_oil_gen(pathToData)
    df_consumtion = load_oil_cons(pathToData)
    define_ratio = 3.15
    # print(df_consumtion.columns[10])
    df2 = df_consumtion.sort_values(2021)
    df2 = df2.drop([np.nan])
    df2 = df2.select_dtypes(exclude=['object', 'datetime']) * define_ratio
    for i in range(0, 65,10):
        df2.iloc[i:i+10,0:56].T.plot()
        
        # plt.title('Million tonnes of CO2 from oil consumed by country')
        # plt.xlabel('Year')
        # plt.ylabel('Million Tonnes') 
        # plt.autoscale
        # plt.show()
        # plt.savefig("plots for oil consumption(CO2 produced)/plot for countries in list" + str(i) + " " + str(i+10))
    return df2



def for_coal():
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    df_consumtion = load_coal_cons(pathToData)
    define_ratio =32
    df2 = df_consumtion.sort_values(2021)
    df2 = df2.drop([np.nan])
    df2 = df2.select_dtypes(exclude=['object', 'datetime']) * define_ratio
    for i in range(0, 65,10):
        df2.iloc[i:i+10,0:56].T.plot()
        
        # plt.title('Million tonnes of CO2 from coal consumed by country')
        # plt.xlabel('Year')
        # plt.ylabel('Million Tonnes') 
        # plt.autoscale
        # plt.show()
        # plt.savefig("plots for coal consumption(CO2 produced)/plot for countries in list" + str(i) + " " + str(i+10))
    return df2


def for_gas():
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    df_generation=load_gas_gen(pathToData)
    df_consumtion = load_gas_cons(pathToData)
    define_ratio = 56
    df2 = df_consumtion.sort_values(2021)
    df2 = df2.replace("-",0)
    df2 = df2.drop([np.nan])
    pd.set_option('display.max_columns', None)
    df2.mul(define_ratio)
    for i in range(0, 65,10):
        df2.iloc[i:i+10,0:51].T.plot()
        
        # plt.title('Tonnes of CO2 by gas consumed by country')
        # plt.xlabel('Year')
        # plt.ylabel('Million Tonnes') 
        # plt.autoscale
        # plt.show()
        # plt.savefig("plots for gas consumption(CO2)/plot for countries in list" + str(i) + " " + str(i+10))
    return df2

def main():
    df_oil = for_oil()
    df_gas = for_gas()
    df_coal = for_coal()
    df_energ = for_energy_total()
    labels = 'Coal','Gas','Rest','Oil'
    # plt.close('all')
    year = 2021
    for i in range(0,df_coal.index.size):
        sizes = [0,0,0,0]
        for year_5 in range(year - 4,year + 1):
            curent_size = [(df_coal.iloc[i][year_5]), float((df_gas.iloc[i])[year_5]), float((df_energ.iloc[i])[year_5]) - float(df_coal.iloc[i][year_5]) - float((df_gas.iloc[i])[year_5]) - float((df_oil.iloc[i])[year_5]), float((df_oil.iloc[i])[year_5])]
            for k in np.arange(len(sizes)): sizes[k] += curent_size[k]
        if all(j>=0 for j in sizes) and not(sum(sizes) == 0):
            explode = (0,0,0.1,0)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
            ax1.axis('equal')
            plt.title("Percentage of CO2 made" + df_coal.index[i])
            plt.savefig("pie charts for CO2/plot for countries in list " + df_coal.index[i] + ".jpeg")
            # plt.close()
            # plt.show()


if __name__=="__main__":
    main()