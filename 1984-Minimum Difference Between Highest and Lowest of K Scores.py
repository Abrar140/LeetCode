class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        minimumarray=[]
        for i in range(len(nums)):
            if (i+k)>len(nums):
                break
            minimumarray.append(nums[i]- nums[i+k-1])
        return min(minimumarray)
            
        return nums