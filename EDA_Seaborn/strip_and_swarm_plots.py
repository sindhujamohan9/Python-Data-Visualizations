import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

housing = data('Housing')
housing_df.head()

sns.catplot(housing_df, y='price', hue='bedrooms')

sns.catplot(housing_df, y='price')

sns.catplot(housing_df, x='bedrooms', y='price', hue='driveway', dodge=True); # strip plot

sns.catplot(housing_df, x='bedrooms', y='price', hue='driveway', kind='swarm');

sns.catplot(housing_df, x='bedrooms', y='price', hue='driveway', kind='swarm', dodge=True, aspect=2);
