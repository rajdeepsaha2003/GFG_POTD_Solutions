
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        temp=s1+s1
        if(len(s1)==len(s2) and s2 in temp):
            return True
        return False