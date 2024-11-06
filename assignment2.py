# Empty list
my_list = []

# Append the four elements to the empty list.
values_to_add = [10, 20, 30, 40]
for value in values_to_add:
    my_list.append(value)
print(my_list)

# Insert 15 in the second position of the list
my_list[1] = 15
print(my_list)

# Extend my_list with another_list
another_list = [50, 60, 70]
my_list.extend(another_list);
print(my_list)

# Remove the last element in the list
del my_list[6]
print(my_list)

# Sorting my_list in ascending order
my_list.sort()
print(my_list)

# Printing the index of value 30
value = 30
index = my_list.index(value);
print(index)
