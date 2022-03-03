def double(x):
    return x*2

# Lambda Functions
# In Python, you can declare a variable of type function, where implementations can be simply assigned

# In some use cases, you may have to function pointer to a function for some processing logic 
# Best Scenario: Callback scenarios
# A mechnism of defining a method implementation as an expression inline
new_double = lambda x: x*2


print(double(10))
print(new_double(200))

def get_value():
    return 10

result = get_value()

print(new_double(result))

print((lambda x: x*x)(10)) # In Python programming, these instructions should be avoided ...

formatter = lambda x, y, z='X': '{}, {}, {}'.format(x, y, z)

print(formatter('R', 'J'))

formatter2 = lambda x, y, *z : '{} {} {}'.format(x, y, max(z))

print(formatter2(10,20,30,40,50))