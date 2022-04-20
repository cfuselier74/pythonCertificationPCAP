# list are mutable

my_list = [1, 5, 3, 4, 2]
print(type(my_list))
print(my_list)

my_list.append("this is a sentence")
print(my_list)

sentence = my_list.pop()

print(my_list)
print(sentence)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list[2:])
print(my_list[2:4])

print(len(my_list))

another_list = ['a', 'b', 'f', 'h']
print(my_list + another_list)

my_list = [1, 2, 3, 5, 2, 3, 6]

count = my_list.count(2)

print(count)