import pandas as pd
import numpy as np

file1 = './one.csv'
file2 = './two.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

new_df = df1.append(df2)

print(new_df)