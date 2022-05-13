a=int(input("enter how many subjects you have?"))
total=0
for i in range(a):
    i=int(input("enter the marks in each subject"))
    total=total+i
    p=float((total/(a*100))*100)
print(p,"is the percentage")
if(p>90 and p<100):
    print("outstanding")
elif(p>80 and p<89):
    print("excellent")
elif(p>70 and p<79):
    print("very good")
elif(p>60 and p<69):
    print("good")
elif(p>50 and p<59):
    print("above")
elif(p>49 and p<40):
    print("average")
elif(p>44 and p<40):
    print("pass")
elif(p<40):
    print(" fail")
