# Declare a list
declared_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(declared_list)

# Display the list in ascending order
sorted_list = sorted(declared_list)
print(sorted_list)
print(declared_list)

# Display the ist in descending order
sorted_desc_list = sorted(declared_list, reverse=True)
print(sorted_desc_list)
print(declared_list)

# Display the even indexes from a list
even_index_list = declared_list
x = slice(0, 10, 2)
print(even_index_list[x])

# Display the odd indexes from a list
odd_index_list = declared_list
x = slice(1, 10, 2)
print(odd_index_list[x])

# Display the multiples of 3 from a list
multiple_list = declared_list
for i in multiple_list:
    if i % 3 == 0:
        print(i)
