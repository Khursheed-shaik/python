# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": [88, 92, 85]
}
print("Original dictionary:", student)

# Accessing values by key
print("Student's name:", student["name"])
print("Student's major:", student["major"])

# Adding a new key-value pair
student["graduation_year"] = 2025
print("After adding graduation year:", student)

# Updating an existing value
student["age"] = 21
print("After updating age:", student)

# Removing a key-value pair
removed_major = student.pop("major")
print("After removing major:", student)
print("Removed major:", removed_major)

# Checking if a key exists in the dictionary
if "name" in student:
    print("Key 'name' exists in the dictionary.")

# Looping through dictionary keys
print("Dictionary keys:")
for key in student.keys():
    print(key)

# Looping through dictionary values
print("Dictionary values:")
for value in student.values():
    print(value)

# Looping through dictionary items (key-value pairs)
print("Dictionary items:")
for key, value in student.items():
    print(f"{key}: {value}")

# Clearing all items in the dictionary
student.clear()
print("Dictionary after clearing:", student)
