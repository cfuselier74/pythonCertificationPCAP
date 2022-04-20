# help(print)

def greet_person(val="Friend"):
    """
    DOCSTRING: this returns a greeting
    INPUT: value
    OUTPUT: hello ... name
    """
    return 'Hello there {0}, this is a greeting...'.format(val)


print(greet_person("Taz"))
print(greet_person())


def get_remainder(num1, num2):
    """
    DOCSTRING: returns the remainder for two numbers
    INPUT: num1, num2
    OUTPUT: 10 % 3 = 1
    """
    return num1 % num2


print(get_remainder(15, 5))
print(get_remainder(15, 2))