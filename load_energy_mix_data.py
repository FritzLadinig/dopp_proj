import pandas as pd

def load_energy_mix_data(csv_path):
    
    # INPUT:
    # csv_path = path to the csv file nrg_bal_s__custom_4360563_linear.csv
    
    # OUTPUT:
    # dataframe df with columns Year, Country Code, Country, Indicator, Value, Flag
    # df contains 3 Indicators: Gross electricity production, Gross heat production and Primary production
    # Flag Z indicated logically non-feasible combinations of energy balance and also combinations that 
    # are not covered by the reporting templates (countries do not report these data points).
    
    source_mapping={'C0000X0350-0370': 'Solid fossil fuels',
                'C0350-0370': 'Manufactured gases',
                'E7000': 'Electricity',
                'G3000': 'Natural gas',
                'H8000': 'Heat',
                'N900H': 'Nuclear heat',
                'O4000XBIO': 'Oil and petroleum products (excluding biofuel portion)',
                'P1000': 'Peat and peat products',
                'RA000': 'Renewables and biofuels',
                'S2000': 'Oil shale and oil sands',
                'TOTAL': 'Total',
                'W6100_6220': 'Non-renewable waste'}
    
    country_mapping={'AL': 'Albania',
                 'AT': 'Austria',
                 'BA': 'Bosnia and Herzegovina',
                 'BE': 'Belgium',
                 'BG': 'Bulgaria',
                 'CY': 'Cyprus',
                 'CZ': 'Czechia',
                 'DE': 'Germany',
                 'DK': 'Denmark',
                 'EA19': 'Euro area-19 countries (2015-2022)',
                 'EE': 'Estonia',
                 'EL': 'Greece',
                 'ES': 'Spain',
                 'EU27_2020': 'European union-27 countries (from 2020)',
                 'FI': 'Finland',
                 'FR': 'France',
                 'GE': 'Georgia',
                 'HR': 'Croatia',
                 'HU': 'Hungary',
                 'IE': 'Ireland',
                 'IS': 'Iceland',
                 'IT': 'Italy',
                 'LT': 'Lithuania',
                 'LU': 'Luxembourg',
                 'LV': 'Latvia',
                 'MD': 'Moldova',
                 'ME': 'Montenegro',
                 'MK': 'North Macedonia',
                 'MT': 'Malta',
                 'NL': 'Netherlands',
                 'NO': 'Norway',
                 'PL': 'Poland',
                 'PT': 'Portugal',
                 'RO': 'Romania',
                 'RS': 'Serbia',
                 'SE': 'Sweden',
                 'SI': 'Slovenia',
                 'SK': 'Slovakia',
                 'TR': 'Turkey',
                 'UA': 'Ukraine',
                 'UK': 'United Kingdom',
                 'XK': 'Kosovo'}
    
    df_energy_mix = pd.read_csv(path_to_energy_mix_data, sep=';')
    df = pd.DataFrame(data=df_energy_mix[["TIME_PERIOD", "geo", "nrg_bal", "siec",
                                      "unit", "OBS_VALUE", "OBS_FLAG"]].values,
                      columns=["Year", "Country Code", "Indicator", "Energy Source",
                               "Unit", "Value", "Flag"])
    df["Country"] = df["Country Code"].apply(lambda x: country_mapping[x])
    df["Energy Source"] = df["Energy Source"].apply(lambda x: source_mapping[x])
    df["Indicator"] = df["Indicator"].apply(lambda x: "Gross electricity production" if (x=="GEP") else x)
    df["Indicator"] = df["Indicator"].apply(lambda x: "Gross heat production" if (x=="GHP") else x)
    df["Indicator"] = df["Indicator"].apply(lambda x: "Primary production" if (x=="PPRD") else x)
    return df

path_to_energy_mix_data = "DataSets/energy_mix.csv"
df = load_energy_mix_data(path_to_energy_mix_data)
print(df.shape)
print(df.head())
