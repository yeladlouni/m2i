import matplotlib.pyplot as plt

with open('../../../data/hr/employees.csv') as f:
    salaries = [float(line.split(';')[7]) for line in f if 'SALARY' not in line]

print(salaries)

# Solution en utilisant la classe Count du package collections

from collections import Counter

salaries_count = Counter(salaries)

print(salaries_count)

# Solution à base des dictionnaires

#salaries_count = {salary: count for salary in salaries}

# En utilisant la fonction count
salaries_count={}
for e in salaries:
    salaries_count[e] = salaries.count(e)

# En utilisant la fonction get du dictionnaire

salaries_count = {}

for e in salaries:
    salaries_count[e] = salaries_count.get(e, 0) + 1

print(salaries_count)

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)


ax1.plot(salaries_count.keys(), salaries_count.values())

ax2.scatter(salaries_count.keys(), salaries_count.values())

ax3 = fig.add_subplot(2, 2, 4)

plt.hist(salaries, bins=20)

plt.show()

# Lorqu'on a des variables continues, on utilise un histogram
