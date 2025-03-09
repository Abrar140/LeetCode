class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        nums.sort()
        return nums
            

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(Solution().transformArray(nums))