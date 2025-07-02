#higherst number out of three

a=int(input("Enter the 1st Number: "))
b=int(input("Enter the 2nd Number: "))
c=int(input("Enter the 3rd Number: "))

if a>b and a>c:
   print(a,"Is Bigger")
elif b>c and b>a:
    print(b,"is Bigger")
else:
    print(c,"is Bigger")
