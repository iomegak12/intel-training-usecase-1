import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

# print(df.isnull().sum())

print(df.shape)

df1 = df.dropna()
df1 = df1.drop_duplicates()

print(df1.shape)


