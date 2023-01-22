from sys import displayhook
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pathlib    


a,b,c,d,e,f,g,h,i = [plt.cm.winter, plt.cm.cool, plt.cm.spring, plt.cm.copper, plt.cm.bone, plt.cm.gist_heat, plt.cm.pink, plt.cm.summer, plt.cm.autumn]

outer_colors = [a(.6), b(.6), c(.6), d(.6), e(.6), f(.6), g(.6), h(.6), i(.6)]
inner_colors = [a(.5), a(.4), 
                b(.5), b(.4), b(.3), b(.2),
                c(.5), c(.4), c(.3),
                d(.5), d(.4),
                e(.5), e(.4),
                f(.5), f(.4),
                g(.5), g(.4),
                h(.7), h(.6), h(.5), h(.4), h(.3), h(.2), h(.1), h(5),
                i(.7), i(.6), i(.5), i(.4), i(.3), i(.2), i(.1)]
def autopct(pct): # only show the label when it's > 10%
    return ('%.2f' % pct) if pct > 5 else ''

def main():
    df = pd.read_csv("ghg-emissions-by-sector.csv")
    pd.set_option('display.max_columns', None)
    df = df.drop(['Code'],axis=1)
    num = df._get_numeric_data()
    num[num<0] = 0
    df = df.fillna(0)
    for country in df.Entity.unique():
        if country!='Niue':
            print(country)
            df_year1 = df[df['Year'] == 2019]
            df_year1 = df_year1[df["Entity"] == country]

            values1 = df_year1.loc[:,df_year1.columns != 'Entity']
            values1 = values1.loc[:,values1.columns != 'Year']
            collumns = values1.columns
            collumns = collumns.to_numpy()
            values1 = values1.to_numpy()



            # Filter the dataframe for the second year
            df_year2 = df[df['Year'] == 2010]
            df_year2 = df_year2[df["Entity"] == country]

            values2 = df_year2.loc[:,df_year2.columns != 'Entity']
            values2 = values2.loc[:,values2.columns != 'Year']
            values2 = values2.to_numpy()



            facecolor = '#eaeaf2'
            font_color = '#525252'
            hfont = {'fontname':'Calibri'}
            size = 0.3
            fig, ax = plt.subplots(figsize=(17,12), facecolor=facecolor)


            ax.pie(values1[0],colors=outer_colors,textprops={'color':font_color}, radius=1, autopct = autopct,wedgeprops=dict(width=size, edgecolor='w'),pctdistance = 1)
            ax.pie(values2[0],radius=0.75, autopct=autopct,colors=outer_colors,wedgeprops=dict(width=size, edgecolor='w'),pctdistance = 0.5)
            # plt.legend(loc=2, prop={'size': 6})
            ax.legend(collumns,loc='upper left', frameon=False)
            ax.set_title('CO2 emmisions by industry in ' + country, fontsize=18, pad=15, color=font_color)
            plt.savefig("pie charts of CO2 per industry/pie for countries in list" + country)



if __name__=="__main__":
    main()