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



def load_gdpData(filepath, countries):
    print(filepath)
    df=pd.read_csv(os.path.join(filepath, "GDP.csv"), sep=",", header=2)
    df=df.rename(columns={"Country Name": "country"})
    df=df.set_index("country")

    df=df.iloc[:,8:-1]
    
    df=df.rename(index={"United States": "US", "Venezuela, RB": "Venezuela", "Czechia": "Czech Republic", "Slovak Republic": "Slovakia", 
            "Turkiye": "Turkey", "Iran, Islamic Rep.": "Iran", "Egypt, Arab Rep.": "Egypt", "Korea, Rep.": "South Korea"})
    cntries=[cntry for cntry in countries if cntry in df.index]
    #print([cntry for cntry in countries if cntry in df.index])
    #print([cntry for cntry in countries if cntry not in df.index])
    df=df.loc[cntries]
    df=df.rename(columns={cols:int(cols) for cols in df.columns})
    df=df.stack()
    df=df.to_frame()
    df=df.rename(columns={df.columns[0]: "GPD"})
    df.index.set_names(["country", "Year"], inplace=True)
    #print(df)
    return df

def load_popData(filepath):
    df=pd.read_excel(os.path.join(filepath, "Population.xlsx"), sheet_name="Estimates", header=16)
    df=df.loc[df["Type"]=="Country/Area"]
    df=df[["Region, subregion, country or area *", "ISO3 Alpha-code", "Year", 'Total Population, as of 1 January (thousands)', 'Life Expectancy at Birth, both sexes (years)']]
    df=df.rename(columns={"Region, subregion, country or area *": "country"})
    df["Year"]=df["Year"].astype(int)
    df=df.set_index("country")
    #df1=df1.loc[[df1["1950"]>=1000]]
    df.to_csv(os.path.join(filepath, "PopReduced.csv"), index=True)
    print(df)
    return df

def load_popRedData(filepath, countries):
    df=pd.read_csv(os.path.join(filepath, "PopReduced.csv"), sep=",", header=0)
    df=df.set_index(["country", "Year"])
    df=df.rename(index={"United States": "US", 'United States of America': "US", "Venezuela, RB": "Venezuela",  'Venezuela (Bolivarian Republic of)': "Venezuela", "Czechia": "Czech Republic", "Slovak Republic": "Slovakia", 
            "Turkiye": "Turkey", 'Türkiye': "Turkey", "Iran, Islamic Rep.": "Iran", 'Iran (Islamic Republic of)': "Iran", "Egypt, Arab Rep.": "Egypt", 
            "Korea, Rep.": "South Korea", 'Republic of Korea': "South Korea", 'Viet Nam': "Vietnam"})
    cntries=list(set(cntry[0] for cntry in df.index if cntry[0] in countries))
    
    df=df.drop(columns=["ISO3 Alpha-code"])
    
    df=df.loc[cntries]
    return df

def main():    
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    #df=load_gdpData(pathToData, countries)
    #df=load_popData(pathToData)
    df=load_popRedData(pathToData, countries)
    print(df)

if __name__=="__main__":
    main()