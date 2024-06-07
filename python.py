import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv("./housing.csv")
df
import matplotlib.pyplot as plt
plt.style.use("bmh")           
fig, ax = plt.subplots()        
plt.plot()                      
import csv
with open('./housing.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)    
        
        
surveys_df = pd.read_csv("./housing.csv")
surveys_df['weight'].describe()
surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()
surveys_df['weight'].std()
surveys_df['weight'].count()

print("[¿Cuáles son estas caracteristicas? ")
print()
print("¿Qué caracteristicas afectan de manera positiva y negativa al precio de la casa?")
print()


grouped_data = surveys_df.groupby('longitude') 
grouped_data.describe() 
grouped_data.mean()
grouped_data = surveys_df.groupby('housingMedianAge') 
grouped_data.describe() 
grouped_data.mean()
grouped_data = surveys_df.groupby('medianHouseValue')
grouped_data.describe()  
grouped_data.mean()
grouped_data = surveys_df.groupby('oceanProximity') 
grouped_data.describe()
grouped_data.mean()

x_values = df['oceanProximity'].unique()
y_values = df['oceanProximity'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.show()
plt.close('all')


df.shape 
df['median_income'].mean() 
sns.scatterplot(x="median_house_value",y="median_income",data=df)
df.hist(bins=50,figsize=(15,15)) 
plt.show()
plt.hist(df["housing_median_age"],color='#FF2331')  
plt.title("housing_median_age- Histogram plot")    
plt.xlabel("housing_median_age")
plt.ylabel("Frequencies")
plt.grid(True)
plt.show()