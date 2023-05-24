import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

housing_df.head()

iris_df = data('iris')
iris_df.head()

sns.pairplot(housing_df, vars=['price', 'lotsize'], size=4)

sns.pairplot(iris_df, hue='Species')

sns.pairplot(iris_df)

sns.pairplot(iris_df, hue='Species')

sns.pairplot(iris_df)

sns.pairplot(iris_df, hue='Species', vars=['Sepal.Length', 'Petal.Length'])

sns.pairplot(iris_df, hue='Species', diag_kind='hist')

sns.pairplot(iris_df, hue='Species', diag_kind='hist', kind='hist')
