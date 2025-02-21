class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        return prod(map(int, str(n)))-sum(map(int, str(n)))
        

n = 234
instance = Solution()
print(instance.subtractProductAndSum(n))