import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

housing_df.head()

plt.boxplot(
    x=housing_df['price'],
    notch=True,
    vert=False,
    showmeans=True,
    whis=1.5, # change whisker size   
   
);
plt.yticks([]) # y vales do not appear

austres_df.head()

austres_df['pct_change'] = austres_df['austres'].pct_change()

plt.plot(austres_df['time'], austres_df['austres']);
plt.plot(austres_df['time'], austres_df['pct_change']);


fig, ax = plt.subplots()
ax.plot(austres_df['time'], austres_df['austres']);
ax.set_title('Australian Population')
ax.set_xlabel('Years')
ax.set_ylabel('Population')
fig.savefig('australian_population.png')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True) #(2,1) -- two plots which are vertically aligned; sharex -- share the x-axis

ax1.plot(austres_df['time'], austres_df['austres'], ls=':');
ax1.set_ylabel('Population')

ax2.plot(austres_df['time'], austres_df['pct_change']);
ax2.set_xlabel('Years')
ax2.set_ylabel('% change')

fig.suptitle('Australian Population')

min_pct_change_y = austres_df['pct_change'].min()
min_pct_change_y
min_pct_change_x = austres_df[austres_df['pct_change'] == min_pct_change_y]['time'].iloc[0]
min_pct_change_x

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True) #(2,1) -- two plots which are vertically aligned; sharex -- share the x-axis

ax1.plot(austres_df['time'], austres_df['austres'], ls=':');
ax1.set_ylabel('Population')

ax2.plot(austres_df['time'], austres_df['pct_change']);
ax2.set_xlabel('Years')
ax2.set_ylabel('% change')

fig.suptitle('Australian Population')
ax2.annotate('What happened here?', xy=(min_pct_change_x, min_pct_change_y), xytext=(min_pct_change_x-8, min_pct_change_y*1.2), arrowprops={})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# First the bar plot
ax1.bar(story_counts.index, story_counts)
ax1.set_xticks(story_counts.index) # see what happens without this
ax1.set_title('Number of stories')
ax1.set_xlabel('Stories')
ax1.set_ylabel('Number of houses')
ax1.grid(axis='y', alpha=0.5, ls=':');

# Pie chart on the right
ax2.pie(story_counts, labels=story_counts.index, autopct='%f') # Try replacing %f with %f%%, then %.f%%, then %.1f%%
ax2.legend()
ax2.set_title('Portions of houses with various stories');

fig.tight_layout()

fig, ax = plt.subplots(2, 2, figsize=(10, 10))

# ax is an object with four axes 0,0 - top left plot, 0,1 - top right plot, so on

ax[0,0].hist(housing_df['price'], bins=10)
ax[0,0].set_ylabel('Price')

ax[0,1].scatter(housing_df['lotsize'], housing_df['price'])

ax[1,0].scatter(housing_df['price'], housing_df['lotsize'])
ax[1,0].set_xlabel('Price')
ax[1,0].set_ylabel('Lot Size')

ax[1,1].hist(housing_df['lotsize'], bins=10)
ax[1,1].set_xlabel('Lot Size')

fig.suptitle('Lotsize and Price Correlogram')
fig.tight_layout(rect=[0, 0, 1, 0.95]);



