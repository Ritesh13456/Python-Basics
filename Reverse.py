#reverse a number
a=int(input("Enter the number: "))

rev=0
while a !=0:
    number=a%10
    rev=rev*10+number
    a=a//10
print(rev)