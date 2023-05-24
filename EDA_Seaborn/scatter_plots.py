import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

housing = data('Housing')
housing_df.head()

# Scatter Plots

sns.relplot(data=housing_df, x='lotsize', y='price', height=10, aspect=2)
plt.title('Lot Size vs Price')
plt.xlabel('Lot size')
plt.ylabel('Price')
plt.annotate('We can add text here', xy=(10000,150000))
plt.axhline(125000)
plt.grid(axis='y',alpha=0.5)

sns.relplot(data=housing_df, x='lotsize', y='price', kind='scatter') # scatter is default relplot

# Divide points based on driveway

sns.relplot(data=housing_df, x='lotsize', y='price', kind='scatter',hue='driveway')

# Divide points based on driveway

sns.relplot(data=housing_df, x='lotsize', y='price', kind='scatter',col='driveway', height=4, aspect=2)

sns.relplot(data=housing_df, x='lotsize', y='price', kind='scatter',col='driveway',row='airco', height=4, aspect=2)

sns.relplot(data=housing_df, 
            x='lotsize', 
            y='price', 
            kind='scatter',
            col='driveway',
            row='airco',
            size='bedrooms',
            hue = 'stories'
          )                         # We can keep adding complexity in the plot


