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
