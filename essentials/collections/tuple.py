my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple2 = (1, 2, 3, (4, 5, 6), (7, 8, 9))
print(my_tuple2)

a, b, c = my_tuple
print(str(a) + ", " + str(b) + ", " + str(c))

values = [1, 2, 3]
m, n, o = values

print(str(m) + ", " + str(n) + ", " + str(o))

print(my_tuple[0]) # accessing indexed item
print(my_tuple[-1]) # first element from the last

my_tuple[0] = 20 # error, because tuple is immutable
print(my_tuple) 