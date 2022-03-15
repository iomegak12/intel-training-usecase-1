import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Unemployment_rate': [6.1, 5.6, 5.7, 8.9, 1.4, 5.6, 7.8],
    'Year': [1999, 2000, 2001, 2002, 2003, 2004, 2005]
}

df = pd.DataFrame(data, columns=data.keys())

df.plot(x = 'Year', y = 'Unemployment_rate', kind = 'line')

plt.show()