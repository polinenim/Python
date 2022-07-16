def bubble_sort(list1):  
    for i in range(0,a-1):  
        for j in range(a-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1
list1=[]
a=int(input("enter"))
for k in range(0,a):
    n=int(input("enter"))
    list1.append (n)
print("The unsorted list is: ", list1)  
print("The sorted list is: ", bubble_sort(list1))  
