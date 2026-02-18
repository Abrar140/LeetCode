class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s==p:
            return True
        for i in range(len(s)):
            if i==len(p):
                return False
            if s[i]!=p[i]:
                if p[i]!=".":
                    if p[i]=="*":
                        return True

                    return False
                
        return True      




s = "aa"
p = "a"
instance = Solution()
print(instance.isMatch(s,p))  