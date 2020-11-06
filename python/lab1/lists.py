# On peut déclarer une variable liste en mettant les différents éléments entre crochets et séparés avec des virgules

alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
employees = ['Dupont', 'Lewis', 'Jean', 'Dedier', 'Albert', 'Camus']
salaries = [1200, 1400, 900, 3200, 2100.0, 1200.2]

print(employees[2])

print(employees[0])

print(salaries[3])

print(salaries[-1])

# Ecrire une instruction pour changer "Dupont" avec "Mathilde"

employees[0] = "Mathilde"

print(employees)

# Ajout d'un nouveau élément à la liste

employees = employees + ["Adele"]

print(employees)

# Fonctions de listes

employees.append("Frederic")  # Permet d'ajouter un élément à la fin de la liste
print(employees)

#employees.clear() # Supprime l'ensemble des éléments de la liste
#print(employees)


# A shallow copy: une copie superficielle de la liste

tmp = employees
print("employees: ", employees)
print("tmp: ", tmp)

tmp[2] = "Jeanette"

print("employees: ", employees)
print("tmp: ", tmp)

# A deep copy/hard copy: copie profonde de la liste

tmp = employees.copy()
print("employees: ", employees)
print("tmp: ", tmp)

tmp[2] = "Jeanette"

print("employees: ", employees)
print("tmp: ", tmp)

# Afficher le nombre d'occurences d'un élément de la liste

print(employees.count("Jeanette"))

# Afficher le nombre d'éléments de la liste

print(len(employees))

# Extend permet d'étendre une liste avec une autre liste

trainees = ["Patrick", "Lionel", "Lara"]

employees.extend(trainees)

print(employees)

# Insérer un élément  dans la liste à la position précisée par le premier élément

employees.insert(3, "Willy")

print(employees)

# Renvoyer l'index de la première occurrence d'un élément

print(employees.index("Dedier"))

# La fonction len permet de retourner le nombre d'éléments de la liste

len(employees)

# La fonction pop permet de retirer un élément de la liste tout en le renvoyant

print(employees)

item = employees.pop()

print(employees)
print(item)

# La fonction remove permet d'enlever un élément de la liste

employees.remove("Willy")

print(employees)

# La fonction reverse permet d'inverse l'ordre des éléments

employees.reverse()

print(employees)

# un mot palindrome est un mot qui peut être lu dans les deux sens, la fonction reverse permet d'inverser l'order de la liste

word = "python"

tmp = list(word)
tmp.reverse()
print(tmp)
print(list(word))
print(tmp == list(word))

# La fonction sort permet de trier les éléments de la liste

employees.sort()

print(employees)

salaries.sort() # tri dans l'ordre numérique

print(salaries)

mylist = [str(i) for i in salaries]
mylist.sort()
print(mylist)

print(300 < 1000)
print(int('300') < int('1000'))
print(ord('3'), ord('1'))

# Fonction de conversion

# list() permet de convertir vers une liste
# str() permet de convertir vers un string
# int() permet de convertir vers un entier
# float() pour convertir vers un nombre décimal

print(2*'30.23')  # 30.2330.23

print('*' * 20)


# Ecrire un script afin de définir une liste de mois
# Afficher les mois dans l'ordre alphabetique
# Afficher les mois dans l'ordre inverse
# Remplacer le mois Juin avec l'équivalent en anglais

months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août',
          'Septembre', 'Novembre', 'Décembre']

print(sorted(months))  # sorted permet de trier la liste sans effet secondaire / side effect

print(list(reversed(months)))  # reversed permet d'inverser la liste sans effet secondre

months[5] = 'June'

print(months)


#  split permet de diviser une chaine de caractères selon un séparateur

days = "Lundi;Mardi;Mercredi;Jeudi;Vendredi;Samedi;Dimanche"

days_list = days.split(';')

print(days_list)

# join permet de joindre les élements d'une list

print('|'.join(employees))

# Afficher les mois de l'année

for month in months:
    print(month)

