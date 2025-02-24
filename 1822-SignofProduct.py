class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product=1
        for i in nums:
            product=product*i
        if product>0:
            return 1
        elif product<0:
            return -1
        else:
            return 0


nums = [-1,-2,-3,-4,3,2,1]
solution = Solution()
print(solution.arraySign(nums))