class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=max(nums)
        minimum=min(nums)
        for i in range(minimum, 0,-1):
            if maximum%i==0 and minimum%i==0:
                return i

        # return [max(nums), min(nums)]



nums = [2,5,6,9,10]
solution = Solution()
print(solution.findGCD(nums))