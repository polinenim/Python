def recur_fibo(n):  
   if n <= 1:  
       return n 
       
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
n= int(input("enter your input "))  
if n <= 0:  
    
   print("Plese enter a positive integer")  
else:  
    
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(recur_fibo(i))
