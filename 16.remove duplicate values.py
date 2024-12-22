numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_numbers = list(set(numbers))

print("List without duplicates:", unique_numbers)



n=input().split(",")
l=[int(a) for a in n]
new=[]
for i in l:
    if i in new:
        continue
    else:
        new.append(i)
print(new)