class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        sums=0
        for i in nums:
            sums=sums+i
            if sums==0:
                count+=1
        return count
           






nums = [2,3,-5]
print(Solution().returnToBoundaryCount(nums))