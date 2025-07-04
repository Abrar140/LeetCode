class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return bin(n).count('1')
        return bin(n)[2:].count('1')




n=11
instance = Solution()
print(instance.hammingWeight(n))