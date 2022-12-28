import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pathlib

def load_gdpData(filepath):
    print(filepath)
    df=pd.read_csv(os.path.join(filepath, "GDP.csv"), sep=",", header=2)
    #print(df)
    return df

def load_popData(filepath):
    df=pd.read_excel(os.path.join(filepath, "Population.xlsx"), sheet_name="Estimates", header=16)
    df=df.loc[df["Type"]=="Country/Area"]
    df=df[["Region, subregion, country or area *", "ISO3 Alpha-code", "Year", 'Total Population, as of 1 January (thousands)', 'Life Expectancy at Birth, both sexes (years)']]
    #print(df)
    return df

def main():    
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    #df=load_gdpData(pathToData)
    df=load_popData(pathToData)
    print(df)

if __name__=="__main__":
    main()