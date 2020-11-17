import pandas as pd

with open('../../data/hr/employees.csv') as f:
    # 1ère méthode en utilisant f.readlines() pour renvoyer la liste des lignes du fichie
    lines = f.readlines()

    columns = 'EMPLOYEE_ID;FIRST_NAME;LAST_NAME;EMAIL;PHONE_NUMBER;HIRE_DATE;' \
              'JOB_ID;SALARY;COMMISSION_PCT;MANAGER_ID;DEPARTMENT_ID'.split(';')

    data = {
        column: {i: line[1:-3].split(';')[j] for i, line in enumerate(lines) if 'EMPLOYEE_ID' not in line}
        for j, column in enumerate(columns)
    }

    df3 = pd.DataFrame(data)

# Afficher les employés qui ont une commission

print(df3[df3['COMMISSION_PCT'] != ''])

# Afficher le salaire pour Jennifer

indice = df3.index[(df3['FIRST_NAME'] == 'Jennifer') & (df3['LAST_NAME'] == 'Whalen')]
print(indice)
print(indice[0])
print(df3.at[indice[0], 'SALARY'])

# Afficher le nom complet des employés qui appartiennent au département 50 et qui ont un salaire > 3000

df3['SALARY'] = df3['SALARY'].astype('float')

emp = df3[(df3['DEPARTMENT_ID'] == '50') & (df3['SALARY'] > 3000)]   #  le & est un bits operator

emp_list = list(emp['FIRST_NAME'] + ' ' + emp['LAST_NAME'])

print(emp_list)

print(df3['DEPARTMENT_ID'] == '50')

# Afficher le nom complet des managers
print('df3', df3)
df4 = pd.DataFrame(df3, index=df3['EMPLOYEE_ID'])
print('df4', df4)
df3.drop(df4[df4['MANAGER_ID'] == ''].index)
print(df4)