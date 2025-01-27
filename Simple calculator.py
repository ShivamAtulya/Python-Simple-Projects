print("*****SIMPLE CALCULATOR*****")
a=int(input("enter first number"))
b=int(input("enter second number"))
choise=int(input("enter your choise from 1 to 4:"))
if choise==1:
    print("1.Addition of a and b is",a+b)
elif choise==2:
    print("2.Subtraction of a and b is",b-a)
elif choise==3:
    print("3.Multiplication of a and b is",a*b)
elif choise==4:
    print("4.Division is a and b is",b/a)   
else:
    print("WRONG INPUT")