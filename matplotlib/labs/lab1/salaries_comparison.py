import matplotlib.pyplot as plt

salaries_shipping, salaries_sales = [], []

with open('../../../data/hr/employees.csv') as f:
    for line in f:
        if line.endswith('50\',\n'):
            salaries_shipping += [float(line.split(';')[7])]
        elif line.endswith('80\',\n'):
            salaries_sales += [float(line.split(';')[7])]

print(salaries_sales, salaries_shipping)

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

ax1.hist(salaries_shipping, bins=20)

ax2.hist(salaries_sales, bins=20)

ax3.scatter(salaries_sales[:10], salaries_shipping[:10])
plt.show()
