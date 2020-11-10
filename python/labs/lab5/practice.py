import pandas as pd

df = pd.read_html('corona.html')[0] # read_html permet de renvoyer la liste des tables contenues dans la page html

#print(df.columns) # la propriété columns permet de renvoyer l'entête d'un dataframe

top_ten= df.sort_values(by=['TotalDeaths'], ascending=False)[2:].head(10)

data_france = df.loc[df['Country,Other'] == 'France']  # Série

population_france = int(data_france['Population'].values[0])
tests_france = int(data_france['TotalTests'].values[0])



print(f"Population: {population_france}\nTests: {tests_france}")

corona_list = df.to_dict('records') # to_dict permet d'obtenir une liste de dictionnaires

print(len(corona_list))

countries_list = [record['Country,Other'] for record in corona_list]

print('World' in countries_list)

for record in corona_list:
    if record['Country,Other'] == 'World' or record['Country,Other'] == 'Total:':
        corona_list.remove(record)

print(len(corona_list))

cases_mean = round(sum([record['TotalCases'] for record in corona_list]) / len(corona_list), 2)

print(cases_mean)

countries_top_cases = [record['Country,Other'] for record in corona_list if record['TotalCases'] >= cases_mean]

print(countries_top_cases)

df.to_json('corona.json', orient='records', lines=True)
