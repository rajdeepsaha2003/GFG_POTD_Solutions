class Solution:
    def columnWithMaxZeros(self, arr, N):
        max = 0
        res = -1
        
        for i in range(N):
            c = 0
            for j in range(N):
                # Counting zeroes
                if arr[j][i] == 0:
                    c += 1
            
            # Updating max_count and ans as required
            if c > max:
                max = c
                res = i
        
        return res