#RIGHT ANGLED TRIANGLE

# Input number of rows
n = int(input("Enter number of rows for triangle pattern: "))

# Constructing the triangle pattern
for i in range(1, n+1):
    print('*' * i)



#PYRAMID

# Input number of rows
n = int(input("Enter number of rows for pyramid pattern: "))

# Constructing the pyramid pattern
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))


#INVERTED RIGHT ANGLED 

# Input number of rows
n = int(input("Enter number of rows for inverted triangle pattern: "))

# Constructing the inverted triangle pattern
for i in range(n, 0, -1):
    print('*' * i)
