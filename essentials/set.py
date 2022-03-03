my_set = {1, 2, 3}
print(my_set)

my_set = {1, 2.0, 3, False, True, "Element v10"}
print(my_set)

my_set2 = {True, 1, 1.01, 2.0, 3, False, 3, 0,
           3, True, "Element v10", "Abram - Starwars"}

my_set2.add(100)
# verify the operation how updates are happening inside
my_set2.update(["Batman v2022", "Inception", False, 230])
my_set2.discard(True)

print(my_set2)

# for value in my_set2:
#     print(value)

list_x = list(my_set2)
print(list_x[2])

index_count = 0
for value in my_set2:
    if index_count == 1:
        print(value)
        break

    index_count += 1
