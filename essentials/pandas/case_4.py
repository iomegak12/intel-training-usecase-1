import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

# loc is a label based, which means that we have to specify the name of the rows and columns
# that we need to filter out

# print(df.loc[1:5])
# print(df.loc[df.Age >= 50])

# iloc is integer index-based, we have to specify rows and columns by their integer index

# print(df.iloc[[100, 200]])

print(df.iloc[15:20, 3:7]) # fetch rows 15 to 19 (20 excluded) and 3rd to 6th column (7th excluded)

print(df.iloc[20][3]) # 20th Row and 3rd Column
