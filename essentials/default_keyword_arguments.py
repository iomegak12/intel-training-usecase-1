def greet(firstName='', middleName='', lastName=''):
    print('Hello, ' + lastName + ', ' + middleName + ' ' + firstName)


greet('Michael', 'G', 'Bay')  # supplying parameters in a specific sequence
greet('Michael', 'G')  # skipping lastName parameter
greet()  # skipping all parameters

# specifying the custom sequence in which parameter values are passed
greet(middleName='J', lastName='Damodaran', firstName='Ramkumar')
