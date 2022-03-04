programmingLanguages = ['C++', 'Python', 'Rust']
list_1 = ['Reading Books', 10, True]
nestedLists = [1, 2, 3, [10, 20, 30], [100, 200, 300]]

print(nestedLists[0])
print(nestedLists[-1])
print(nestedLists[3][0])

name = ['R', 'A', 'M', 'K', 'U', 'M', 'A', 'R']
# start from offset 2 and till offset 5 excluding 5
print(name[2:5])

# start from offset 2 till the end
print(name[2:])

print('\n')
print(name[:])
print(name)
print('\n')

# changing the offset 2
name[2] = 'J'

print(name)

print('\n')
name[2:5] = ['A', 'B', 'C', 'D']
print('\n')

print(name)

name.append('X')
# it appends as a nested list at the end of name variable
name.append(['F', 'G', 'H'])
print(name)

# it flattens the list of values and appended in the name variable
name.extend(['I', 'J', 'K'])

print(name)

values = [10, 50, 20, 30, 67, 22]
values.sort()
print(values)

values_a = [1, 2, 3, 4, 3, 4, 5]
values_b = [10, 20, 30, "40", False]
result = values_a + values_b

print(result)

result.remove(False)
print(result)

print(values_a.__len__())
print(values_a.count(3))  # searches value 3
print(values_a.index(3))  # first index

namex = ['z', 'b', '6', '0', '01', '20']
print(namex)
namex.sort()
print(namex)
