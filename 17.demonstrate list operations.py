# Initializing a list
numbers = [10, 20, 30, 40, 50]
print("Initial list:", numbers)

# Adding elements to the list
numbers.append(60)  # Adds 60 to the end
print("After appending 60:", numbers)

numbers.insert(2, 25)  # Inserts 25 at index 2
print("After inserting 25 at index 2:", numbers)

# Removing elements from the list
numbers.remove(40)  # Removes the first occurrence of 40
print("After removing 40:", numbers)

popped_element = numbers.pop()  # Removes the last element and returns it
print("After popping the last element:", numbers)
print("Popped element:", popped_element)

# Finding the length of the list
length = len(numbers)
print("Length of the list:", length)

# Sorting the list
numbers.sort()  # Sorts in ascending order
print("Sorted list:", numbers)

numbers.sort(reverse=True)  # Sorts in descending order
print("List sorted in descending order:", numbers)

# Slicing the list
print("Slicing from index 1 to 3:", numbers[1:4])

# Reversing the list
numbers.reverse()
print("Reversed list:", numbers)

# Counting occurrences of an element
count_of_30 = numbers.count(30)
print("Count of 30 in the list:", count_of_30)

# Clearing the list
numbers.clear()
print("List after clearing all elements:", numbers)
