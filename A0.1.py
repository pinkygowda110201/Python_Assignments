#Arithmetic operators

x=20
y=10

print("x+y=",x+y)
print("x-y=",x-y)
print("x*y=",x*y)
print("x/y=",x/y) #returns quotient
print("x%y=",x%y) #modulo n returns remainder
print("x**y=",x**y) #exponentiation
print("x//y=",x//y) #return integer value

#Assignment operators

a=5

print(a)
a+=5
print(a) #equivalent to a=a+5
a=5
a-=5
print(a) #equivalent to a=a-5
a=5
a*=5
print(a) #equivalent to a=a*5
a=5
a/=5
print(a) #equivalent to a=a/5

#Comparison operators (< > <= >= ==)

if x>y :
    print(x," is greater than ",y)
if y>x :
    print(y," is greater than ",x)
if x>=y :
    print(x," is greater than or equal to ",y)
if x<=y :
    print(x," is lesser than or equal to ",y)
if x==y :
    print(x," is equal to ",y)

#Logical operators (and or not)

x=2
y=4
if x==2 and y==4 :
    print("Yes")
if x==2 and y==2 :
    print("No")
if x==0 and y==2 :
    print("No")
if x==2 or y==4 :
    print("yes")
if x==2 or y==2 :
    print("yes")
if x==0 or y==2 :
    print("No")
