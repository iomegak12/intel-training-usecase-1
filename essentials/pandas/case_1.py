import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

"""
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.info())
"""

# print(df["Gender"])

print(df[["Gender", "Age", "Balance"]].head(10))

