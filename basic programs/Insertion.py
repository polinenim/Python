def insertion_sort(list1):  
  
        for i in range(1, len(list1)):  
  
            value = list1[i]  
  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value  
        return list1  

list1=[]
a=int(input("enter"))
for k in range(0,a):
    n=int(input("enter"))
    list1.append (n) 
print("The unsorted list is:", list1)  
  
print("The sorted list1 is:", insertion_sort(list1))
