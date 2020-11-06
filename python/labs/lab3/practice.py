# Python permet d'ajouter des structures conditionnelles afin d'exécuter des actions lorsqu'une condition est vérifier
# if est l'instruction utilisée pour tester des conditions

cars = ['Audi', 'BMW', 'Mercedes', 'Peugeot', 'Renault', 'Honda', 'Toyota']

# Solution en utilisant les boucles

for car in cars:
    if len(car) > 4:
        print(car)

# Solution en utilisant un comprehension list

cars_five = [car for car in cars if len(car) > 4 or len(car) < 5]

print(cars_five)

for car in cars:
    if car == 'Audi':
        print(car.lower())
    elif car == 'Toyota':
        print(car.title())
    elif car == 'Honda':
        print(car[:2])
    else:
        print(car.upper())


cars_processed = [car.lower() for car in cars if car == 'Audi']



