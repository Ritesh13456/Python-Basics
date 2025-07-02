# #Count number of digits
a=int(input("ENter the number: "))
count=0
while a!=0:
    a=a//10
    count+=1
print(count)