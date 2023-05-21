import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

housing.head()

housing.plot(
    y = 'price',
    kind = 'box'

);

housing.plot(
    y = ['price', 'lotsize'], 
    kind = 'box'

);

housing.boxplot(
    column = ['price'], 
    by = 'bedrooms',
    grid = False
);
