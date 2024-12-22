n=input().split(",")
numbers=[int(a) for a in n]


max_freq_num = None
max_freq = 0
for num in set(numbers):  
    freq = numbers.count(num)  
    if freq > max_freq:  
        max_freq = freq
        max_freq_num = num

print("Element with highest frequency:", max_freq_num)
print("Highest frequency:", max_freq)
