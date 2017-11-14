name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

new_dict = {}
animal_name = zip(name,favorite_animal)
print animal_name
new_dict = dict(animal_name)
print new_dict