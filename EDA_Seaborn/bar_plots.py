import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

housing_df.head()

sns.catplot(data=housing_df, x='bedrooms', y='price', kind='bar')

sns.catplot(data=housing_df, x='bedrooms', y='price', kind='bar', ci=False)

sns.catplot(data=housing_df, x='bedrooms', y='price', kind='bar', ci=False, hue='driveway')

sns.catplot(data=housing_df, x='bedrooms', kind='count')



