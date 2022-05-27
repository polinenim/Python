string = input("Enter the string : ")
strList=list(string) 
output=''.join(sorted(strList, reverse =True)) 
print("String Sorted in ascending order :", output)
