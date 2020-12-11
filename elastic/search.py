from pprint import pprint

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


# Création d'un handle vers le cluster ElasticSearch

es = Elasticsearch(
    'local'
)

# Pour renvoyer le résultat sous forme d'un JSON = Lightweight search

res = es.search(index='hr', doc_type='employee')

# To prettify the result
#pprint(res)

# Pour renvoyer le résultat sous forme d'un objet python = Search DSL

s = Search(using=es, index='hr', doc_type='employee')
s.execute()

for hit in s:
    print(hit.first_name, hit.last_name, hit.age)