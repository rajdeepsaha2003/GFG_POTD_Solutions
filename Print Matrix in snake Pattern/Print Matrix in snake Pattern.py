#User function Template for python3

class Solution:
    
    def snakePattern(self, input_matrix): 
        n = len(input_matrix)
        result = []
    
        for i in range(n):
            if i % 2 == 0:
                for j in range(n):
                    result.append(input_matrix[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    result.append(input_matrix[i][j])
    
        return result