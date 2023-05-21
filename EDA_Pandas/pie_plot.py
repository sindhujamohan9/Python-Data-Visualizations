import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

housing = data('Housing')

story_counts = housing['stories'].value_counts()
story_counts.plot(
    kind = 'pie',
    title = 'Number of stories'
);


