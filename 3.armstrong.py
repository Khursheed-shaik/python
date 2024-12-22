n=int(input("enter the number:"))
str_n=str(n)
length=len(str_n)
sum_cubes=sum(int(i)**length for i in str_n)
if(n==sum_cubes):
    print("armstrong number")
else:
    print("not a armstrong")