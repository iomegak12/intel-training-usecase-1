pow2 = []

for x in range(1, 10):
    pow2.append(2 ** x)

print(pow2)

new_pow2 = [2 ** x for x in range(1,10)] # Comprehensions
print(new_pow2)

new_pow3 = [2 ** x for x in range(1,10) if x % 2 == 0] # Comprehensions with IF
print(new_pow3)

power = lambda x: 2 ** x
conditional_values = [1,2,3,4,5]
new_pow4 = [power(x) for x in range(1,10) if x in conditional_values]
print(new_pow4)

new_pow5 = [power(x) for x in range(1,10) if conditional_values.count(x) >= 1]
print(new_pow5)

