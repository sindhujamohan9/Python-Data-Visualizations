import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

housing = data('Housing')
housing_df.head()

sns.catplot(housing_df, x='bedrooms', y='price', kind='box')

sns.catplot(housing_df, x='bedrooms', y='price', kind='violin')

sns.catplot(housing_df, x='bedrooms', y='price', kind='box', hue='driveway')

sns.catplot(housing_df, x='bedrooms', y='price', kind='violin', hue='driveway', split=True)
