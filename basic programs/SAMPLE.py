arr = []
n = int(input("enter size of array : "))
for i in range(n):
    i=int(input("enter element of array : "))
    arr.append(i)
largest = arr[0]
smallest = arr[0]
for i in range(n):
    if arr[i]>largest:
        largest = arr[i]
    if arr[i]<smallest:
        smallest = arr[i]
print("flargest element in array is:",largest)
print("fsmallest element in array is:",smallest) 
