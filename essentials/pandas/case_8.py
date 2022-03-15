import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

# print(df.sort_values('Balance', ascending = False).head(10))

print(df.sort_values(["Balance", "EstimatedSalary"], ascending=[True, False]).head(10))
