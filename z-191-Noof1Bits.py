class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return bin(n).count('1')
        print(to_binary(n))




n=11
instance = Solution()
print(instance.hammingWeight(n))