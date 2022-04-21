animal = 'test'

if animal == 'cow':
    print("eats grass")
elif animal == 'bird':
    print('eats seeds')
elif animal == 'monkey' or animal == 'ape':
    print('eats bananas')
else:
    print("we don't know what {0} eats".format(animal))
