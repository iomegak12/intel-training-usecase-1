from random import randrange


def get_conditional_values():
    values = [randrange(1, 10), randrange(1, 10), randrange(1, 10)]
    return values

power = lambda x: 2 ** x
conditional_values = get_conditional_values()
powered_values = [power(x) for x in range(1,10) if x in conditional_values]

print(conditional_values)
print(powered_values)