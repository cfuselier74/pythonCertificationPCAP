# tuples are immutable

my_tuple = (1, 2, 3, "some data", [1, 2, 3])

# my_tuple[2] = 4  will not work as tuple cannot be changed

# works because you are changing the value of a list not the tuple.
my_tuple[4][2] = 'new value'

print(my_tuple)
