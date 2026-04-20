#IMPORT LIBRARY
import pandas as pd

#-----------------
#LOAD DATASET
#-----------------

df = pd.read_csv('AirQuality.csv',sep=';')
print('file has downloaded')

#Remove last two empty columns
df = df.iloc[:,:-2]

print("First 5 rows:")
print(df.head())

print('\nDataset Info:')
print(df.info())

#------------------
#DATA CLEANING
#------------------
import numpy as np
df['CO(GT)'] = df['CO(GT)'].astype(str)
df['CO(GT)'] = df['CO(GT)'].str.replace(',', '.')
df['CO(GT)'] = pd. to_numeric(df['CO(GT)'],errors='coerce')
# Replace -200 with NaN (missing values)
df = df.replace(-200, np.nan,inplace=True)
#drop rows with missing values
df.dropna(inplace=True)
print("\nAfter Cleaning:")
df.info()
print("remaining -200:",(df['CO(GT)'] == -200).sum())
print(df['CO(GT)'].min())
print(df['CO(GT)'].head())

#BASIC ANALYSI
#-----------------
print('\nStatistical Summary:')
print(df.describe())

#Average values of key pollutants
df['NO2(GT)'] =pd. to_numeric(df['NO2(GT)'],errors='coerce') 
print("\nAverage CO level:",
    df['CO(GT)'].mean())
print("Max NO2 level:",
     df['NO2(GT)'].max())

#CONVERT Date + Time into single datetime column
df['Datetime'] = pd.to_datetime(df['Date']
+ ' ' + df['Time'],format = "%d/%m/%Y %H.%M.%S", dayfirst=True)

# sort by time
df = df.sort_values(by= 'Datetime')

#IMPORT LIBRARY
import matplotlib.pyplot as plt

#---------------------
# DATA VISUALIZATION
#--------------------

#----Plot 1 : CO Trend-----

plt.figure()
plt.plot(df['Datetime'],
df['CO(GT)'].astype(float))
plt.title("CO Levels over time")
plt.xlabel("Time")
plt.ylabel("CO (mg/m^3)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
 #Changing datatype of columns
cols_to_fix = ['CO(GT)','NO2(GT)','C6H6(GT)']
for col in cols_to_fix :
    df[col] = df[col].astype(str).str.replace(',','.').astype(float)

#------Plot 2 : Polluntant Comparison-----
plt.figure()
plt.plot(df['Datetime'],
df['CO(GT)'].astype(float),label='CO')
plt.plot(df['Datetime'],
df['NO2(GT)'].astype(float),label='NO2')
plt.plot(df['Datetime'],
df['C6H6(GT)'].astype(float),label='Benzene')
plt.title("Pollution Comparison over time")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

 #------Plot 3 : Temperature vs CO ------

plt.figure()
plt.scatter(df['Datetime'],
df['CO(GT)'].astype(float))
plt.title("Temperature vs CO Levels")
plt.xlabel("Temperature (Celsius)")
plt.ylabel("CO")
plt.tight_layout()
plt.show()

#------------------
#KEY INSIGHTS
#------------------

print("\nKey Insights:")
print("1. CO levels fluctuate significantly over time, indicating variable pollution exposure.")
print("2. NO2  and benzene show trends  similar to CO ,suggesting common pollution sources.")
print("3. Temperature appears to influence pollutant concentration patterns.")