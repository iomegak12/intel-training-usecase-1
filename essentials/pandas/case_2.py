import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

# print(df[1:5]) # select a range of rows using loc
# print(df.loc[1:5]) # select a range of rows using loc

print(df.loc[df["Age"] >= 45].head(5)) # filtering