my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1, 2, 3, 4, 5]

my_list.sort()
my_list.reverse()

another_list.reverse()

result = my_list[-3:] + another_list[-3:]
print(result)
