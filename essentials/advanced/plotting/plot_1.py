import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Unemployment_rate': [6.1, 5.6, 5.7, 8.9, 1.4, 5.6, 7.8],
    'Country': ['India', 'United States', 'Australia', 'Germany', 'France', 'Canada', 'Mexico'],
    'Stock_Index_Price': [1500, 1200, 5600, 1200, 1900, 3940, 3400]
}

df = pd.DataFrame(data, columns=data.keys())

df.plot(x='Country', y='Stock_Index_Price', kind='scatter')

plt.show()