a=input("enter a sentence")
b=a.split()
m=b[0]
for i in b:
    if (len(i)>len(m)):
        m=i
print(m,len(m))
