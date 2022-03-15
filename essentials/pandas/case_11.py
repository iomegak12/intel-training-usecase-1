import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

pivoted_table = df.pivot_table(
    index=['Gender', 'Geography', 'Surname'],
    values=['Age', 'Balance'],
    aggfunc='min').sort_values(by=['Age'], ascending=False)

print(pivoted_table)
