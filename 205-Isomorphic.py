class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letterdict={}
        index=0
        for key, value in enumerate(s):
            if index>=len(s):
                break
            if s[index] not in letterdict:
                key=s[index]
                if t[index] in letterdict.values():
                    return False
                value=t[index]
                letterdict[key]=value
                index=index+1
            elif s[index] in letterdict:
                if letterdict[s[index]]!=t[index]:
                    return False
                index=index+1
        return True





s ="foo"
t ="bar"
instance = Solution()
print(instance.isIsomorphic(s,t))  