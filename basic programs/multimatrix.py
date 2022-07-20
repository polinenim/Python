A = [[5, 4, 3],  
     [9, 3, 6],  
     [4, 7, 9]]    
B = [[4, 2, 4],  
     [4, 3, 6],  
     [2, 6, 5]]   
multiplication = [[0, 0, 0],    
               [0, 0, 0],    
               [0, 0, 0]]  
for m in range(len(A)):    
   for n in range(len(B[0])):    
          for o in range(len(B)):    
               multiplication[m][n] += A[m][o] * B[o][n] 
print("The multiplication of matrix A and B is: ")  
for res in multiplication:    
   print(res)
