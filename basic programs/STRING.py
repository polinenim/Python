a = input("Enter a name : ") 
result=''
for i in a:  
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  
        i = ''  
    result += i 
print("after removing the vowels :",result)
