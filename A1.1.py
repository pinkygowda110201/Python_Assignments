#Calculator(using if conditions)
print("1. Add\n2. Subtract")
x=int(input("Enter your choice:"))
if x>2 :
    print("Wrong choice")
else :
    n1=int(input("Enter the 1st number:"))
    n2=int(input("Enter the 2nd number:"))
    if x==1 :
        print("Result after adding : ",n1,"+",n2,"=",n1+n2)
    else :
        print("Result after subtracting : ",n1,"-",n2,"=",n1-n2)
