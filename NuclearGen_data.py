import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pathlib

def load_NuclearGenData(filepath):
    df=pd.read_excel(os.path.join(filepath, "bp-stats-review-2022-all-data.xlsx"), sheet_name="Nuclear Generation - TWh", header=2)
   
    print(df)
    return df

def main():    
    pathToData=os.path.join(pathlib.Path(__file__).parent.resolve(), "DataSets")
    #df=load_gdpData(pathToData)
    df=load_NuclearGenData(pathToData)
    print(df)

if __name__=="__main__":
    main()