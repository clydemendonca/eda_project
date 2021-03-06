# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    for i in range(0, len(num_cols)):
        column = num_cols[i]
        sns.distplot(data[column], hist=True, kde=False)




