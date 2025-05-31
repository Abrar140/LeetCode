class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        if len(s)<len(target):
                return 0
        lst = list(s)
        i=True
        count=0
        while i:
            for alpha in target:
                if alpha not in lst:
                    return count//len(target)
                else:
                    lst.remove(alpha)
                    count+=1
        
      
        

# s = "ilovecodingonleetcode"
s="codecodecodecode"
target = "code"

instance = Solution()
print(instance.rearrangeCharacters(s, target))