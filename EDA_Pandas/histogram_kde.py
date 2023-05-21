import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

# histogram

housing.plot(
    kind = 'hist',
    y = 'price',
    bins = 25,
    legend = False
);

# KDE

housing.plot(
    y = 'price',
    kind = 'kde',
    legend = False,
    xlim = (0, 250000) 
);
