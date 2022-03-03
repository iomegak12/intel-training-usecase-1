x = 10

def my_function():
    global x 
    x = "XYZ"
    print('Value of X is : %s' % x)

my_function()

print(x)