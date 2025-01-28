import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exponent = math.log(n, 2)
        print(exponent)
        return exponent.is_integer()
        
n=536870912
instance = Solution()
print(instance.isPowerOfTwo(n))