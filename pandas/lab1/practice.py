import pandas as pd

with open('../../data/hr/employees.csv') as f:
    # 1ère méthode en utilisant f.readlines() pour renvoyer la liste des lignes du fichie
    lines = f.readlines()

    print(lines)

    data = {
        'EMPLOYEE_ID': pd.Series([line[1:-3].split(';')[0] for line in lines if 'EMPLOYEE_ID' not in line]),
        'FIRST_NAME': pd.Series([line[1:-3].split(';')[1] for line in lines if 'EMPLOYEE_ID' not in line]),
        'LAST_NAME': pd.Series([line[1:-3].split(';')[2] for line in lines if 'EMPLOYEE_ID' not in line]),
        'EMAIL': pd.Series([line[1:-3].split(';')[3] for line in lines if 'EMPLOYEE_ID' not in line]),
        'PHONE_NUMBER': pd.Series([line[1:-3].split(';')[4] for line in lines if 'EMPLOYEE_ID' not in line]),
        'HIRE_DATE': pd.Series([line[1:-3].split(';')[5] for line in lines if 'EMPLOYEE_ID' not in line]),
        'JOB_ID': pd.Series([line[1:-3].split(';')[6] for line in lines if 'EMPLOYEE_ID' not in line]),
        'SALARY': pd.Series([line[1:-3].split(';')[7] for line in lines if 'EMPLOYEE_ID' not in line]),
        'COMMISSION_PCT': pd.Series([line[1:-3].split(';')[8] for line in lines if 'EMPLOYEE_ID' not in line]),
        'MANAGER_ID': pd.Series([line[1:-3].split(';')[9] for line in lines if 'EMPLOYEE_ID' not in line]),
        'DEPARTMENT_ID': pd.Series([line[1:-3].split(';')[10] for line in lines if 'EMPLOYEE_ID' not in line])
    }

    df1 = pd.DataFrame(data)

    print(df1)

    # Pour être concis, on peut utiliser l'alternative suivante:

    with open('../../data/hr/employees.csv') as f:
        # 1ère méthode en utilisant f.readlines() pour renvoyer la liste des lignes du fichie
        lines = f.readlines()

        columns = 'EMPLOYEE_ID;FIRST_NAME;LAST_NAME;EMAIL;PHONE_NUMBER;HIRE_DATE;' \
                  'JOB_ID;SALARY;COMMISSION_PCT;MANAGER_ID;DEPARTMENT_ID'.split(';')

        data = {
            column: [line[1:-3].split(';')[i] for line in lines if 'EMPLOYEE_ID' not in line]
                    for i, column in enumerate(columns)
        }

        df2 = pd.DataFrame(data)

        print(df2)

# En utilisant un dictionnaire de dictionnaires

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

        print(df3)

# Eliminer les employés n'appartenant à aucun département
import numpy as np

# flager les lignes dont le département est vide
df4 = df3[df3['DEPARTMENT_ID'] != '']
print(df4)

# En utilisant np.nan
df3[df3.DEPARTMENT_ID == ''] = np.nan
df5 = df3.dropna()

print(df5)