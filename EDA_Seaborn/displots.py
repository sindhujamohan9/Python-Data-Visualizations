import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

housing_df.head()

sns.displot(housing_df, x='price')

sns.displot(housing_df, x='price', kind='kde')

sns.displot(housing_df, x='price', kind='hist', kde=True)

sns.displot(housing_df, x='price', kind='hist', rug=True)

sns.displot(housing_df, x='price', kind='hist', rug=True, kde=True)

# ECDF - Emp. Cum. Dist. Fn

sns.displot(housing_df, x='price', kind='ecdf')

sns.displot(housing_df, x='price', hue='bedrooms')

sns.displot(housing_df, x='price', hue='bedrooms', multiple='stack')

sns.displot(housing_df, x='price', hue='bedrooms', multiple='dodge')

sns.displot(housing_df, x='price', hue='airco', multiple='stack') # look better when there are less elements in hue

sns.displot(housing_df, x='price', hue='bedrooms', palette='colorblind') # better color contrast

sns.displot(housing_df, x='price', hue='bedrooms', palette='colorblind', element='step')

sns.displot(housing_df, x='price', hue='bedrooms', palette='colorblind', element='step', multiple='dodge')

# kde plot

sns.displot(housing_df, x='price', kind='kde',hue='bedrooms', palette='colorblind')
