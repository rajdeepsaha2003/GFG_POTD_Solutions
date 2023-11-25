#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
 
        curr_max = 0
      
        last_entry = 0
        i = 0
        ans=''
 
        while i < len(S): 
      
            noOfNextD = 0
            if S[i] == "I": 
      
                j = i + 1
                while j < len(S) and S[j] == "D": 
                    noOfNextD += 1
                    j += 1
                if i == 0: 
                    curr_max = noOfNextD + 2
                    last_entry += 1
      
                    ans+=str(last_entry)
                    ans+=str(curr_max)

                    last_entry = curr_max 
                else: 
       
                    curr_max += noOfNextD + 1
      
                   
                    last_entry = curr_max
                    ans+=str(last_entry)

               
                for k in range(noOfNextD): 
                    last_entry -= 1
                    ans+=str(last_entry)
                    i += 1
      
            
            elif S[i] == "D": 
                if i == 0: 
      
                    j = i + 1
                    while j < len(S) and S[j] == "D": 
                        noOfNextD += 1
                        j += 1
      
                    
                    curr_max = noOfNextD + 2
      
                     
                    ans+=str(curr_max)
                    ans+=str(curr_max - 1)


                     
                    last_entry = curr_max - 1
                else: 
      
                     
                    ans+=str(last_entry-1)
                    last_entry -= 1
            i += 1
        return ans