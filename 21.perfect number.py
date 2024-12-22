# Input from the user
number = int(input("Enter a number: "))

# Initialize the sum of divisors
sum_of_divisors = 0

# Loop to find divisors and calculate their sum
for i in range(1, number):
    if number % i == 0:  # Check if i is a divisor
        sum_of_divisors += i

# Check if the sum of divisors is equal to the original number
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
