from pprint import pprint

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


# Création d'un handle vers le cluster ElasticSearch

es = Elasticsearch(
    'localhost'
)

# Pour renvoyer le résultat sous forme d'un JSON = Lightweight search
es.index()

res = es.search(index='hr', doc_type='employee')

# To prettify the result
#pprint(res)

# Pour renvoyer le résultat sous forme d'un objet python = Search DSL

s = Search(using=es, index='hr', doc_type='employee')
s.execute()

for hit in s:
    print(hit.first_name, hit.last_name, hit.age)

doc = {
    'id': 1,
    'first_name': 'test',
    'last_name': 'test',
    'age': 30,
    'interests': ['sport', 'hiking', 'biking']
}

es.index(index='hr', doc_type='employee', body=doc)