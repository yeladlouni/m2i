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

dummies = pd.get_dummies(data['category'], prefix='cat')

data1 = data.join(dummies)

data2 = data.iloc[np.random.permutation(data.index)]

print(data2)
