
# Variables strings

message = "Hello Hello!"

print(message)

# Changer la casse

first_name = "dupont"
last_name = "lewis"

# La fonction title permet de convertir les initiaux d'une chaîne de caractères en majuscules

print(first_name.title())

message = "hello world!"

print(message.title())

# Afficher le first_name en majuscules

print(first_name.upper())

# Afficher le first_name en minuscules

print(first_name.lower())

# Afficher le first_name concaténé avec last_name

print(first_name + " " + last_name)

# On peut aussi utiliser ce qu'on appelle les f-strings, le f dénote format

print(f"Le nom complet est: {first_name.title()} {last_name}.")

# Ecrire une commande python afin d'afficher le first_name et le last_name avec les initiaux en majuscules: Dupont Lewis

print(f"Le nom complet est: {first_name.title()} {last_name.title()}")

# On peut utiliser les espaces "whitespaces" afin de formater le code avec des espaces, tabulation et retours à la ligne
# \n permet le retour à la ligne "new line"
# \t permet d'ajouter une tabulation "tabulation"
# \n et \t sont appelés caractères d'échappement "Escape caracters"

print(f"Le nom complet est:\n \t {first_name.title()} {last_name.title()}")

message = "Ceci est un texte avec un espace à la fin     "

print(message.rstrip())

message = "\n\t    Ceci un message avec un retour à la ligne, une tabulation est des espaces."
print(message)
print(message.lstrip())

# Ecrire une instruction Python afin de retirer les espaces du début et de la fin de la variable message

message = "\n\t\t\n    Ceci est un message avec des espaces au début et des espaces à la fin.\n\n   \t"

