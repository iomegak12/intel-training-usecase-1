def greet(*args, **kwargs):
    """
        In Python Functions,
            * in the parameter section, indicates that you can supply variable number of arguments
            ** in the parameter section, indicates that you can supply
                    keyword arguments with name=value pair as a dictionary
    """

    print('Processing Variable Number of Arguments ...')
    for arg in args:
        print('Argument : ' + arg)

    for key, value in kwargs.items():
        print('Key : ' + key + ', Value ; ' + value)


greet('10', '20', '30', id='E10001', name='Rajkumar', location='Bangalore')
