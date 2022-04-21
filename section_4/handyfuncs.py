list_a = ['a', 'b', 'c', 'd', 'e', 'f']
list_b = [1, 2, 3, 4, 5, 6]
list_c = [99, 98, 97, 96, 95, 94]

print('z' in list_a)
print('a' in list_a)

zipped_list = list(zip(list_a, list_b, list_c))

print(zipped_list)

for a, b, c in zipped_list:
    print(a)
    print(b)
    print(c)

print(min(list_a))
print(max(list_a))

print(min(list_b))
print(max(list_b))
