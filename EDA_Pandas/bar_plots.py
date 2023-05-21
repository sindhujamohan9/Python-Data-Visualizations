import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

# Bar plot for number of bed rooms
bedroom_counts = housing.groupby('bedrooms')['bedrooms'].count()


bedroom_counts.plot(
    kind='bar',
    title='Bed room counts',
    xlabel = '# bedrooms',
    ylabel = 'counts'
    
    );
