class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        list=[-1,0,1]
        number=0
        for index, x in enumerate(nums):
            if index==len(nums)-1:
                return True
            number=nums[index]-nums[index+1]
            if number not in list:
                return False
        return True

nums = [1,2,2,3]

instance = Solution()
print(instance.isMonotonic(nums))  