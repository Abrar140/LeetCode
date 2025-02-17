class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n % 2 == 0 else n * 2


n=5
instance = Solution()
print(instance.smallestEvenMultiple(n))