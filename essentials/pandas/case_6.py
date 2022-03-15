import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

# processed_df = df.rename(columns={"Geography": "Nation"})

# print(processed_df.Nation.head(5))

# print(df.iloc[0][6])

# df.loc[df[0][6]] = [58]

# # df.iloc[1][6] = 58

# print(df.iloc[0])

# replace the value of 0th row and 6th & 7th column values with 58 and 5
# df.loc[[0],6:8] = [58,5]

# df.loc[df.CustomerId == 15634602, df.columns.get_loc(
#     "Age"):df.columns.get_loc("Age")+1] = 58

df.loc[df.CustomerId == 15634602, "Age"] = 58
    # "Age"):df.columns.get_loc("Age")+1] = 58

print(df.loc[df.CustomerId == 15634602])
