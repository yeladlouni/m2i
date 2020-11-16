import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
#import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set(** {
    'title': 'Crise mondiale 2008'
})

data = pd.read_csv('spx.csv', index_col=0, parse_dates=True)

spx = data['SPX']

print(spx.values)

spx.plot(ax=ax, style='k--')

date = datetime(2009, 2, 1)

ax.annotate(text='Peak', xy=(date, 686), xytext=(date, 1490),
            arrowprops=dict(facecolor='red', headwidth=4, width=2, headlength=4),
            horizontalalignment='left', verticalalignment='top')

ax.add_patch(plt.Circle((datetime(2002, 10, 1), 786), 50, color='r'))

plt.show()

plt.savefig('')

