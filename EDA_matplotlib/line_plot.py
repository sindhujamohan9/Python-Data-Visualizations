import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

austres_df = data('austres')
austres_df.head()

plt.figure(figsize=(10,4))
plt.title('Australian Resident Population')
plt.xlabel('Year')
plt.ylabel('Population (in thousands)')
plt.plot(austres_df['time'], austres_df['austres']);

plt.figure(figsize=(10,4))
plt.plot(austres_df['time'], austres_df['austres'], label='Population');
plt.title('Australian Resident Population')
plt.xlabel('Year')
plt.ylabel('Population (in thousands)')
plt.legend()


plt.figure(figsize=(10,4))
plt.plot(austres_df['time'], austres_df['austres'], label='Population');
plt.plot(austres_df['time'], austres_df['austres']+1000, label='Population+1000');
plt.title('Australian Resident Population')
plt.xlabel('Year')
plt.ylabel('Population (in thousands)')
plt.legend()


plt.figure(figsize=(10,4))
plt.plot(austres_df['time'], austres_df['austres'], label='Population');
plt.plot(austres_df['time'], austres_df['austres']+1000, label='Population+1000'); # can plot any number of lines
plt.title('Australian Resident Population')
plt.xlabel('Year')
plt.ylabel('Population (in thousands)')
plt.legend()

# alpha gives opacity of grid lines; 
# axis=y gives horizontal grid lines; 
# ls=':' gives dotted lines
plt.grid(axis='y', alpha=0.3, ls=':') 
