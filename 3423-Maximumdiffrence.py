class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=  float('-inf')
        for i in range(len(nums)):
            if i==len(nums)-1:
                if abs(nums[i]- nums[0])>max:
                    max=abs(nums[i]- nums[0])
            else:
                if abs(nums[i]- nums[i+1])>max:
                    max= abs(nums[i]- nums[i+1])
        return max


nums=[1,2,4]
instance=Solution()
print(instance.maxAdjacentDistance(nums))
