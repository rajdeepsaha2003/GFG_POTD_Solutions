#User function Template for python3



class Solution:
    
    def sumTriangles(self,matrix, n):
        up = 0 
        lo = 0 
        
        for i in range(n):
            for j in range(n):
                
                if(i == j):
                    up += matrix[i][j];
                    lo += matrix[i][j];
                    
                
                elif (j>i):
                    up += matrix[i][j]; 
                
                elif(j<i):
                    lo += matrix[i][j]; 
             
                