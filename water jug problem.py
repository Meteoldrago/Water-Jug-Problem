X=int(input("Enter the value for holder 1:"))
Y=int(input("Enter the value for holder 1:"))
Z=int(input("Enter the value for jug:"))
x=0
y=0

while Z<X<Y:
    print(x,y)

    if x==0:
        for i in range(0,X):
           if x==X:
               break
           x+=1
    if not(y==0):
        print(x, y)

    for i in range(0,x):
        if y==Y:
            print(x, y)
            y=0
            break
        y+=1
        x-=1
    if x==Z or y==Z:
        print("Completed")
        break
