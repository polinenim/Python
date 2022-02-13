a=int(input("enter the number::"))
b=int(input("enter the number::"))
for i in range(a,b+1):
    c=0
    for j in range(1,b+1):
        if (i%j==0):
            c=c+1
    if(c==2):
        print("the number is prime::",i)
