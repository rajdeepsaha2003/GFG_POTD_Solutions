class Solution:
	def isEulerCircuitExist(self, V, adj):
		#Code here
		evens = 0
        odds = 0
        for i in range(V):
            if len(adj[i]) % 2 == 1:
                odds += 1
            else:
                evens += 1
        
        if evens == V:
            return 2
        elif odds <= 2:
            return 1
        else:
            return 0