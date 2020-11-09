import pandas as pd

#Ecrire un script pour afficher le nombre de lignes pour les 5 fichiers yelp

employees = pd.read_json('./data/sample.json')

print(len(employees))