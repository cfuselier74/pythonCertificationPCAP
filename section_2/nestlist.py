my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', 'banana'], 'd']

print(my_list[6][2])

my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
print(my_list[6][2][1])

print(my_list)

my_list[2] = 'computer'
print(my_list)

my_list[6][2][1] = 'joel'
print(my_list)