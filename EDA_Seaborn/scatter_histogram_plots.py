import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

iris_df = data('iris')
iris_df.head()

sns.jointplot(iris_df, x='Sepal.Length', y='Petal.Length')

sns.jointplot(iris_df, x='Sepal.Length', y='Petal.Length', hue='Species') 

sns.jointplot(iris_df, x='Sepal.Length', y='Petal.Length', hue='Species', kind='hist') 

sns.jointplot(iris_df, x='Sepal.Length', y='Petal.Length', hue='Species', kind='hist') 
