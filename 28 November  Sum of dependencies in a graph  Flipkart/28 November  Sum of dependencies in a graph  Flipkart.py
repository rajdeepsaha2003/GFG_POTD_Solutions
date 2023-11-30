class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        sum_val = 0
        for i in range(V):
            s = len(adj[i])
            sum_val += s
        return sum_val