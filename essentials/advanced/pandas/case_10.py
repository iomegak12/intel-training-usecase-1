import pandas as pd
import numpy as np

fileName = './Churn_Modelling.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

df = pd.read_csv(fileName)

# grouped_employees = df[['Gender', 'NumOfProducts']].groupby('Gender')

# aggregated_result = grouped_employees.agg(['mean', 'max', 'min'])

# print(aggregated_result)

grouped_employees = df[['Gender', 'Geography', 'EstimatedSalary', 'Balance']].groupby([
                                                                         'Gender', 'Geography'])

aggregated_result = grouped_employees.agg(['min', 'max'])

print(aggregated_result)