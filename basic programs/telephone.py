#creating a telephone directory
def options():
    print("1.add")
    print("2.search")
    print("4.update")
    print("5.view")
    print("6.exist")
options()
d={}
ch=0
while(ch!=6):
    ch=int(input("enter a one choice"))
    if ch==1:
        name=input("enter name")
        num=int(input("enter a number"))
        d[name]=num
    elif ch==2:
        name=input("enter name")
        if name in d:
            print("the number is",d[name])
        else:
            print("not exist")
    elif ch==3:
        name=input("enter name")
        if name in d:
            del d[name]
        else:
            print("not exist")
    elif ch==4:
        name=input("enter name")
        num=int(input("enter a number"))
        d.update({name:num})
    elif ch==5:
        print(d)
    elif ch==6:
        options()
    
        
                  
                 
    
           
           
