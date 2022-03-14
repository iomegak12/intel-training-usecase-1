import numpy as np
import pandas as pd

data = np.array(['Ramkumar', 'Sunil', 'Sugata', 'Sherif', 'Shah', 'Chloe'])

series = pd.Series(data, index=[i for i in range(100, 700, 100)])

print(series)
