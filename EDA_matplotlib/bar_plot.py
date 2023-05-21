import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

housing_df = data('Housing')
housing_df.head()

bedroom_counts = housing_df.groupby('bedrooms')['bedrooms'].count()
bedroom_counts

plt.bar(
    x=bedroom_counts.index,
    height=bedroom_counts,  
 );

plt.title('Houses by Number of Bed Rooms')
plt.xlabel('# Bed rooms')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.4, ls=':')

# descending order

bc_desc = bedroom_counts.sort_values(ascending=False)
plt.bar(
    x=bc_desc.index,
    height=bc_desc,  
 );

plt.title('Houses by Number of Bed Rooms')
plt.xlabel('# Bed rooms')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.4, ls=':')

# Matplotlib sorts x values automatically, hence we will have to change x to a string using
# x=bc_desc.index.astype('str')


# descending order after converting x values to strings

bc_desc = bedroom_counts.sort_values(ascending=False)
plt.bar(
    x=bc_desc.index.astype('str'),
    height=bc_desc,  
 );

plt.title('Houses by Number of Bed Rooms')
plt.xlabel('# Bed rooms')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.4, ls=':')

# line plot with cumulative sum of number of bedrooms

bc_desc = bedroom_counts.sort_values(ascending=False)
plt.bar(
    x=bc_desc.index.astype('str'),
    height=bc_desc,  
 );
plt.plot(bc_desc.index.astype('str'), np.cumsum(bc_desc), 'o-r', alpha=0.3)
plt.title('Houses by Number of Bed Rooms')
plt.xlabel('# Bed rooms')
plt.ylabel('Count')
plt.axhline(400, ls=':', alpha=0.5)  # can draw a reference line
plt.grid(axis='y', alpha=0.4, ls=':')

# horizontal bar plot 

bc_desc = bedroom_counts.sort_values(ascending=False)
plt.barh(
    y=bc_desc.index,
    width=bc_desc,
    color = 'grey'  
 );
plt.title('Houses by Number of Bed Rooms')
plt.ylabel('# Bed rooms')
plt.xlabel('Count')
plt.grid(axis='x', alpha=0.4, ls=':')
