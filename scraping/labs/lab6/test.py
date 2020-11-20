



def show():
    data = []
    items = ['Audi', 'BMW', 'Mercedes']
    for i, item in enumerate(items):
        data.append({'make': item, 'production': 2000 + i})

    return data

print(show())