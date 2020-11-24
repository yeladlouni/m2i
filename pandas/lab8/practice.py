import numpy as np
import pandas as pd

df = pd.DataFrame({'France': np.random.randint(0, 50, 1000), 'Italie': np.random.randint(0, 50, 1000),
                   'Allemagne': np.random.randint(0, 50, 1000), 'Espagne': np.random.randint(0, 50, 1000)})


#print(df.describe())

#df[(df > 40).any(1)] = 40

print(df[df > 40].all(1))

#print(df.describe())

dataset_test = df.sample(int(len(df) * 0.25))
dataset_train = df.sample(int(len(df) * 0.75))

print(dataset_test.shape)
print(dataset_train.shape)
