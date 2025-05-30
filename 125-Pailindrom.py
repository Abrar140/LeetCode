import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=re.sub('[^a-zA-Z0-9]','',s)
        print(len(s))
        p=s
        s=list(s)
        # print(p,s)
        for x in range(len(s)//2):
            s[x],s[len(s)-x-1]=  s[len(s)-x-1], s[x]
        s="".join(s)    
        if s==p:
            return True
        else:
            return False  




# Example usage
s="0P0"
instance = Solution()
print(instance.isPalindrome(s))  