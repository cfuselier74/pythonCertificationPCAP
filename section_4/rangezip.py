word = 'hello'

for char in list(word):
    print(char)


num = [1, 2, 3, 4, 5]

for n in num:
    print(n)


for n in range(2, 11, 2):
    print(n)

words = ["hello", "my", "name", 'is', 'chris']

combinedItems = zip(num, words)
print(combinedItems)

for item in combinedItems:
    print(item)

for item in enumerate(words, 1):
    print(item)
