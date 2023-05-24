import seaborn as sns
import pandas as pd
import numpy as np
from pydataset import data 

# Styles

iris_df = data('iris')
iris_df.head()

housing_df = data('Housing')
housing_df.head()

sns.set_style('darkgrid')
sns.relplot(data=iris_df, x='Petal.Length', y='Petal.Width', hue='Species')

sns.displot(data=iris_df, x='Petal.Length')

with sns.axes_style('whitegrid'):
  sns.displot(data=iris_df, x='Petal.Length')

with sns.axes_style('dark', {'ytick.left':True}):  # add ticks on the y-axis
  sns.relplot(data=iris_df, x='Petal.Length', y='Petal.Width', hue='Species')
  
# Context

sns.set_context('notebook')
sns.relplot(data=iris_df, x='Petal.Length', y='Petal.Width', hue='Species')

sns.set_context('poster')
sns.relplot(data=iris_df, x='Petal.Length', y='Petal.Width', hue='Species')

sns.set_context('paper')
sns.relplot(data=iris_df, x='Petal.Length', y='Petal.Width', hue='Species')

sns.set_context('talk')
sns.relplot(data=iris_df, x='Petal.Length', y='Petal.Width', hue='Species')

# Color Palettes

sns.relplot(data=housing_df, x='lotsize', y='price', hue='bedrooms', palette='bright')

sns.relplot(data=housing_df, x='lotsize', y='price', hue='bedrooms', palette='pastel')

sns.relplot(data=housing_df, x='lotsize', y='price', hue='bedrooms', palette='colorblind')

sns.color_palette('flare')

sns.color_palette('rocket')

sns.color_palette('vlag')

sns.color_palette('icefire')

# Themes

sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)
sns.catplot(housing_df, x='bedrooms', y='price', kind='box')

sns.set_theme(context='paper', style='darkgrid', palette='pastel', font='sans-serif', font_scale=1, color_codes=True, rc=None)
sns.catplot(housing_df, x='bedrooms', y='price', kind='box')

sns.set_theme(context='paper', style='darkgrid', palette='pastel', font='serif', font_scale=1, color_codes=True, rc=None)
sns.catplot(housing_df, x='bedrooms', y='price', kind='box') # change fonts



  
  
