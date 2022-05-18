for i in range(1,1000):
    b=i
    s=0
    while b>0:
        r=b%10
        s=s+r**3
        b=b//10
    if (s==i):
        print(i,"is a amstrong number")
