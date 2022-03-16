import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Unemployment_rate': [6.1, 5.6, 5.7, 8.9, 1.4, 5.6, 7.8],
    'Year': [1999, 2000, 2001, 2002, 2003, 2004, 2005],
    'Country': ['India', 'United States', 'Australia', 'Germany', 'France', 'Canada', 'Mexico']
}

df = pd.DataFrame(data, columns=data.keys())

df.plot.barh(x='Country', y='Unemployment_rate', color='green')

plt.show()
