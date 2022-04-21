from random import randint
from random import shuffle

ran_num = randint(0, 1000)

print(ran_num)

mylist = [1, 2, 3, 4, 5]
shuffle(mylist)

print(mylist)

mylist2 = list(range(101))
shuffle(mylist2)
print(mylist2)
