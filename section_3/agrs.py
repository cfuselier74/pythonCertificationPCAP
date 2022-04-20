result = sum((1, 2, 3, 4, 5))

print(result)


def my_sum(*args):
    return sum(args)


print(my_sum(1, 10, 5, 6, 6, 7, 8))


def key_value_func(**kwargs):
    print(kwargs.values())
    print(kwargs.get('name'))
    print(kwargs.get('weight'))
    print(kwargs.get('age'))
    print(kwargs.get('address'))


key_value_func(name='mike', weight=200, age=27)
