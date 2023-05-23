import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

housing_df.head()

nile_df = data('Nile')

nile_df.head()

sns.relplot(nile_df, x='time', y='Nile', kind='line')

salaries_df = data('Salaries')
salaries_df.head()

sns.relplot(salaries_df, x='yrs.service', y='salary', kind='line', aspect=2) 
# explanation of figure: dark line - average, light areas: conf. interval; for a single point, seaborn makes no Conf. interval

# Without Conf. interval

sns.relplot(salaries_df, x='yrs.service', y='salary', kind='line', aspect=2, ci=False) 

sns.relplot(salaries_df, x='yrs.service', y='salary', kind='line', aspect=2, ci=False, hue='sex') 

sns.relplot(salaries_df, x='yrs.service', y='salary', kind='line', aspect=2, ci=False, hue='discipline') 

sns.relplot(salaries_df, x='yrs.service', y='salary', kind='line', aspect=2, ci=False, col='sex', hue='discipline') 
