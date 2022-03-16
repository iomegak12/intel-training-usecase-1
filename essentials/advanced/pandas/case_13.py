import pandas as pd
import numpy as np

employee_file = './one.csv'
skill_file = './three.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

employee_df = pd.read_csv(employee_file)
skill_df = pd.read_csv(skill_file)

processed_df = employee_df.join(
    skill_df.set_index('id'),
    on='id',
    how='inner')

print(processed_df)
