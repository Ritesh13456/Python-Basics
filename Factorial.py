a=int(input("Enter the number: "))

if a<0:
    print("negative value has no factorial")
elif a==0:
    print(1)
else:
 b=1
 for x in range(1,a+1):
    b*=x
 print(b)
