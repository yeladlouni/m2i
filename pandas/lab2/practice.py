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

df4 = df3.copy()

df4['NAME'] = df4['FIRST_NAME'] + ' ' + df4['LAST_NAME']

df4.drop(columns=['FIRST_NAME', 'LAST_NAME'], inplace=True)

print(df4.columns)
