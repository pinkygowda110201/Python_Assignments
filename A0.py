#Write algorithm for finding x and y : 10,1,8,3,6,5,4,7,x,y
for p in range(1,11) :
    if p%2==0 :
        p=p-1
        n=p
    else :
        p=p-1
        n=10-p
    print(n)

#"end" in print function of python
print("Hello",end=" !")
print("\nThis is Pinky",end=" ;)")
