n1=int(input("Enter the total no.of plots: "))
f=e=o=0
l=[]
if n1<=20 and n1>=1:
    print("Enter the numbers of each plot")
    for i in range(n1):
        i=int(input())
        if i<=0:
            print("Invalid Input")
            exit()
        l.append(i)
        o=(sum([i for i in l if i%2!=0]))
        e=sum([i for i in l if i%2==0])
        avg=float((e+o)/2)
    print("The password for the file is: %.2f" % avg)
else:
    print("invalid input")