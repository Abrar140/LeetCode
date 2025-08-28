class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        if n == 1:
            return True
        while n >= 0:
            
            if n % 2 != 0 or (n / 2) != int(n / 2):
                break
            if n / 2 == 1:
                return True
            
            n = n / 2

        return False
            
       
        
n=3
instance = Solution()
print(instance.isPowerOfTwo(n))