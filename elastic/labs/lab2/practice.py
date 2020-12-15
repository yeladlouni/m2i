import pandas as pd


credits = pd.read_csv('data/credits.csv', header=0)
movies = pd.read_csv('data/movies_metadata.csv', header=0)

print(credits.head())
print(movies.head())

#df = pd.merge(credits, movies)

#df.to_csv('data.csv')
