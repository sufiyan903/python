a=int(input("enter the side 1:"))
b=int(input("enter the side 2:"))
c=int(input("enter the side 3:"))
if((a+b>c)and(b+c>a)and(c+a>b)):
   print("triangle is possible")
else:
   print("triangle is not possible")
