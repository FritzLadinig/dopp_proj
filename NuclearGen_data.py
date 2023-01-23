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

def load_NuclearGenData0(filepath):
    df=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Nuclear Generation - TWh", header=2)
    df=df.rename(columns={"Terawatt-hours": "country"})
    
    df=df.set_index("country")
    df=df.loc[countries]
    df=df.fillna(0.0)
    
    return df

def load_NuclearGenData(filepath, countries):
    df=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Nuclear Generation - TWh", header=2)
    df=df.rename(columns={"Terawatt-hours": "country"})
    
    df=df.set_index("country")
    df=df.loc[countries]
    df=df.loc[:, 1965:2021]
    df=df.stack()
    df=df.to_frame()
    df=df.rename(columns={df.columns[0]: 'Nuclear Generation - TWh'})
    df.index.set_names(["country", "Year"], inplace=True)
    df=df.fillna(0.0)
    
    return df

def load_CoalCons(filepath, countries):
    df=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Coal Consumption - EJ", header=2)
    df=df.rename(columns={"Exajoules": "country"})
    
    df=df.set_index("country")
    df=df.loc[countries]
    df=df.loc[:, 1965:2021]
    df=df.stack()
    df=df.to_frame()
    df=df.rename(columns={df.columns[0]: "Coal consumption - EJ"})
    df.index.set_names(["country", "Year"], inplace=True)
    df=df.fillna(0.0)
    
    return df


def plotNuclearGen(df):
    df.plot()

def main():    
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    #df=load_gdpData(pathToData)
    #df=load_NuclearGenData(pathToData, countries)
    df=load_CoalCons(pathToData, countries)
    print(df)

if __name__=="__main__":
    main()