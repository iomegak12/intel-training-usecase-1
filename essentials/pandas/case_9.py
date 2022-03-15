import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

premium_employees = df[(df['CreditScore'] > 700) & (df['CreditScore'] < 900)]
sorted_premium_employees = premium_employees.sort_values(['CreditScore'], ascending=True)

print(sorted_premium_employees[["RowNumber", "Surname", "CreditScore"]])

