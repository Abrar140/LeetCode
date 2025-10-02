class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        minmumarray=[]
        for i in  range(0, len(nums), 2):
            minmumarray.append(min(nums[i], nums[i+1]))
            
        return sum(minmumarray)
        





nums = [6,2,6,5,1,2]
Solution