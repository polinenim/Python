a=input("enter a sentence")
b={}
c={}
k=a.split()
for i in a:
    b[i]=a.count(i)
print(b)
for j in k:
    c[j]=k.count(j)
print(c)
