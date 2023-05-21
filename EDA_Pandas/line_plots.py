import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

print('ways to import datasets')

# mc12 = pd.read_csv('/content/Two+Machines.csv')

# # in-built datasets in seaborn

# sns.get_dataset_names()
# sns.load_dataset('tips')

# # in-built datasets in seaborn

# sns.get_dataset_names()
# sns.load_dataset('tips')

# # Using Pydatasets

# housing = data('Housing')
# housing = data('diamonds')

housing = data('Housing')

housing.plot()

housing.plot(
    y = 'price',
    title = 'House Prices',
    xlabel = 'House Index',
    ylabel = 'Price',
    legend = False,
    figsize = (20, 10)
);



housing.plot(
    y = ['price','lotsize'],
    title = 'House Prices',
    xlabel = 'House Index',
    ylabel = 'Price',
    legend = False,
);


housing.plot(
    y = ['price','lotsize'],
    title = 'House Prices',
    xlabel = 'House Index',
    ylabel = 'Price',
    legend = False,
    subplots = True
);


housing.plot(
    y = ['price','lotsize'],
    title = 'House Prices & Lot Sizes',
    xlabel = 'House Index',
    subplots = True
);

# line plot is the default plot in pandas

housing.plot(
    y = ['price','lotsize'],
    title = 'House Prices & Lot Sizes',
    xlabel = 'House Index',
    subplots = True,
    layout = (1, 2),     # 1 row, 2 columns
    figsize = (20, 7)   # width = 20, height  = 7
);

housing.plot(
    y = ['price','lotsize'],
    title = 'House Prices & Lot Sizes',
    xlabel = 'House Index',
    subplots = True,
    layout = (1, 2)   # 1 row, 2 columns
);

plt.tight_layout()

nile = data('Nile')
nile.head()

nile.plot(
    x = 'time',
    y = 'Nile',
    title = 'Nile River Flow Analysis',
    xlabel = 'Year',
    ylabel = 'Flow',
    legend = False,
    subplots = True

);
