class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[0]+nums[2]>nums[1]:
            if nums[0]==nums[1] and nums[1]==nums[2] and nums[2]==nums[0]:
                return "Equilateral"
            elif nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Not A Triangle"
nums=[2,2,3]
solution=Solution()
print(solution.triangleType(nums))