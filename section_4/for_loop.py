farm_animals = ['goat', 'horse', 'chicken', 'cow', 'dog']

for animal in farm_animals:
    count = farm_animals.index(animal) + 1
    sentence = "{0}: {1} is safe in our farm".format(str(count), animal)
    print(sentence)

# lets compiler know we will implement later
for item in farm_animals:
    pass

