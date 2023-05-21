import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

housing.plot(
    x = 'lotsize',
    y = 'price',
    kind = 'scatter'
)
