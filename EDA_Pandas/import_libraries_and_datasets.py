import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

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

housing
