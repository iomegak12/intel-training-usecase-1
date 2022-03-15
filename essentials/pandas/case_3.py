import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

print(df.describe())
print(df["Age"].mean())
print(df.Age.mean())
print(df.Age.unique())
print(df.Geography.unique())

