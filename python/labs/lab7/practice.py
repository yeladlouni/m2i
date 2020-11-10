

with open('../../../data/hr/departments.csv') as f:
    departments = f.readlines()

with open('../../../data/hr/employees.csv') as f:
    employees = f.readlines()

import json

with open('employees.json', 'w') as f:
    json.dump({'id': 10, 'first_name': 'king'}, f)

with open('employees.json') as f:
    employees = json.load(f)
    print(employees['id'])