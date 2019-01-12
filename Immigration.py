import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

df_can.isnull().sum()

#Cleaning the data set to remove a few unnecessary columns
df_can.drop(['Type','Coverage','AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)

#Renaming the columns
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)

df_can['Total'] = df_can.sum(axis=1) #Summing up the total immigrants by country

#Making a list of years
df_can.columns = list(map(str, df_can.columns)) # converting the column names into strings
years = list(map(str, range(1980, 2014))) # declaring a new variable

df_can.set_index('Country', inplace=True) # setting the "Country" as the index.

#Top 5 countries
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_can.to_csv('ModifiedData.csv') #Save dataframe
df_top5 = df_can.head(5)
df_top5 = df_top5[years].transpose() 
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

