import pandas as pd
import numpy as np

data = pd.DataFrame({'product': ['macbook', 'hp deskjet', 'canon', 'ipad', 'iphone 12', 'samsung s20', 'xbox'],
                     'price': [1500.00, 100.12, 500.99, 350.50, 569.99, 600.20, 330.12]})

product_category = {
    'MacBook': 'computer',
    'HP Deskjet': 'computer',
    'Canon': 'photography',
    'iPad': 'computer',
    'iPhone 12': 'phones',
    'Samsung s20': 'phones',
    'XBox': 'gaming'
}

product_category = {key.lower():value for key, value in product_category.items()}

data['category'] = data['product'].map(lambda x: product_category[x.lower()])

np.random.seed(123)


def get_serial(x):
    sample = 10 * np.random.sample(10)
    sample = [str(int(x)) for x in sample]
    return x.upper()[0] + ''.join(sample)


# En utilisant une sample
data['serial'] = data['category'].map(get_serial)

# En utilisant randint
data['serial2'] = data['category'].map(lambda x: x.upper()[0] + ''.join([str(np.random.randint(0, 10)) for _ in range(10)]))

# Rencommer l'index
data.index = data.index.map(lambda x: 'Ligne ' + str(x + 1))

# Mettre en majuscule les intitulés de colonnes
data.columns = data.columns.map(lambda x: x.upper())
print(data)