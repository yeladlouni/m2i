# import matplotlib.pyplot as plt
import pandas as pd
#
data = pd.read_csv('california_housing_train.csv')
#
#
# variables = ['total_bedrooms', 'total_rooms', 'population', 'households', 'median_income', 'housing_median_age']
#
# fig, axes = plt.subplots(6, 6, sharex=True, sharey=True)
#
# for i in range(6):
#     for j in range(6):
#         axes[0, j].set_title(variables[j])
#         print(i, j)
#         axes[i,j].scatter(data[variables[i]], data[variables[j]])
#
#
#
# plt.show()


# En utilisant seaborn, un package qui se base sur matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('california_housing_train.csv')

g = sns.PairGrid(data[['median_income', 'total_rooms', 'total_bedrooms', 'households', 'population']], hue='total_rooms')

g.map(sns.scatterplot)

plt.show()
