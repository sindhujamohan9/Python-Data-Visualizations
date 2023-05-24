import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

iris_df = data('iris')
iris_df.head()

sns.lmplot(data=iris_df, x='Sepal.Length', y='Petal.Length')

sns.lmplot(data=iris_df, x='Sepal.Length', y='Petal.Length', ci=False)

sns.lmplot(data=iris_df, x='Sepal.Length', y='Sepal.Width', ci=False)

sns.lmplot(data=iris_df, x='Sepal.Length', y='Petal.Length', ci=False, hue='Species')

sns.jointplot(iris_df, x='Sepal.Length', y='Petal.Length', kind='reg')

sns.pairplot(iris_df, kind='reg', hue='Species')

