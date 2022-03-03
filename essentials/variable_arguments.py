def greet(*names):
    """
    in python, * indicates in the parameter section, that you can supply variable
    number of arguments
    """

    for name in names:
        print('Hello, ' + name)


greet('Rob', 'Sunil', 'Chloe')
