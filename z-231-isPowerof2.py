import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n>=0:
            if n%2!=0:
                n=n/2
            print(n)
       
        
n=536870912
instance = Solution()
print(instance.isPowerOfTwo(n))