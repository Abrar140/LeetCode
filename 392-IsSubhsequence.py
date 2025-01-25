class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        else:
            letterdict={index:letter for index,letter in enumerate(s)}
        letterindex=0
        for  x in t:
            
            if x==letterdict[letterindex]:   
                if letterindex==len(s)-1:
                    return True
                letterindex=letterindex+1
                if letterindex==len(s):
                    return False
        return False       



        




s = "abc"
t = "ahbgdc"
instance = Solution()
print(instance.isSubsequence(s,t))  