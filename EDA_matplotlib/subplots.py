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
