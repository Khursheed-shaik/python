# Creating a tuple
my_tuple = (10, 20, 30, 20, 40, 50, 20)

print("Original tuple:", my_tuple)

# Accessing elements by index
print("Element at index 2:", my_tuple[2])

# Slicing the tuple
print("Slice from index 1 to 4:", my_tuple[1:5])

# Finding the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)

# Counting occurrences of an element in the tuple
count_20 = my_tuple.count(20)
print("Count of 20 in the tuple:", count_20)

# Finding the index of an element in the tuple
index_30 = my_tuple.index(30)
print("Index of 30 in the tuple:", index_30)

# Checking for existence of an element
if 40 in my_tuple:
    print("40 is in the tuple")

# Concatenating two tuples
another_tuple = (60, 70)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Repeating the tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)
