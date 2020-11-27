#!/usr/bin/env python

import sys
import math

(last_key, max_val) = (None, -math.inf)  # Les variables last_key et max_val permettent de stocker la valeur maximale pour chaque année
for line in sys.stdin: # On lit l'entrée strandard stdin pour récupérer l'année et le température (key,val), ou alors on utilise < pour lire à partir d'un fichier
  # Pour la sortie standard, on utilise le pipe | pour passer le résultat à un programme ou le signe de redirection > pour stocker le résultat dans un fichier
  (key, val) = line.strip().split("\t")  # Le map avait envoyé les données sous forme de tuples print(%s\t%s) ou prinf(f"{key}\t{val}), le reduce récupère les données pour les traiter ligne par ligne en splitant la ligne avec tabulation comme séparateur
  if last_key and last_key != key: # Si la clé "année" n'a pas déjà été rencontrée, la températeur maximale est celle extraite à partir de la ligne
    print(f"{last_key}\t{max_val}") # On affiche sur l'écran le résultat, comme on peut aussi utiliser > pour stocker sur un fichier
    (last_key, max_val) = (key, int(val)) # On met à jour la dernière clé/année et la valeur maximale
  else:
    (last_key, max_val) = (key, max(max_val, int(val))) # Si la valeur de la clé "année" a été déjà rencontrée, on compare la valeur de la ligne en cours avec la températeur maximale

if last_key:
  print("%s\t%s" % (last_key, max_val))


# Sur windows, on peut piper avec la commande:
# python max_temperature_map.py < "c:\Users\yelad\Hadoop-MapReduce\NCDC weather files\1901" | python max_temperature_reduce.py