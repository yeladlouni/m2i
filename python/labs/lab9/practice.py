import json

with open('../../../data/hr/employees.csv') as f:
    employees = [[field for field in line.split(';')] for line in f]


with open('../../../data/hr/employees.csv') as f:
    employees = [
        {
            'first_name': line[1:-3].split(';')[1],
            'last_name': line[1:-3].split(';')[2],
            'department_id': line[1:-3].split(';')[10]
        }
        for line in f if not line.startswith('\'EMPLOYEE_ID')
    ]

with open('../../../data/hr/departments.csv') as f:
    departments =  { line[1:-3].split(';')[0]: line[1:-3].split(';')[1] for line in f if not line.startswith('\'DEPARTMENT_ID') }

print(departments['10'])

# Pour écrire un fichier CSV

output = [e['first_name'] + '\t' + e['last_name'] + '\t' + departments[e['department_id']] + '\n' for e in employees if e['department_id']]

with open('output.csv', 'w') as f:
    f.writelines(output)

# Pour écrire un fichier JSON

output = [
    {
        'first_name': e['first_name'],
        'last_name': e['last_name'],
        'department_name': departments[e['department_id']]
    }
    for e in employees if e['department_id']
]

with open('output.jsonl', 'w') as f:
    json.dump(output, f)
