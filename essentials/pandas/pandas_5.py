import pandas as pd
import numpy as np
data = {
    'Id': [1, 2, 3, 4, 5],
    'Name': ['Syed', 'Shah', 'Sunil', 'Sherif', 'Sugata'],
    'Score': [100, 200, 250, 350, 275]
}

df = pd.DataFrame(
    data, index=['Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5'])

df["Locations"] = np.array(
    ['Bangalore', 'New York', 'Houston', 'Boston', 'Sydney'])

print(df["Name"])

print(df)