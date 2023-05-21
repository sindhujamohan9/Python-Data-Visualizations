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
    whis=1.5,               # change whisker size   
   
);
plt.yticks([])              # y vales do not appear
