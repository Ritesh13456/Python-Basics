# Fibbonachi

x=int(input("ENter the number: "))
a=0
b=1
fibb=[]
if x==0 or x==1:
    print(0)
elif x==2:
    print(0,1)
else:
 fibb.append(a)
 fibb.append(b)

 for i in range(2,x):
    next_fib=a+b
    fibb.append(next_fib)
    a=b
    b=next_fib
 print(fibb)
