class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ouput_array=[]
        for indexx, x  in enumerate(nums):
            for indexy ,y in enumerate(nums[indexx+1:], start=indexx+1):
                if x==y:
                    ouput_array.append((indexx,indexy))

        return len (ouput_array)
nums = [1,1,1,1]
instance=Solution()
print("the good pairs are",instance.numIdenticalPairs(nums))
# print("the good pairs are",instance.numIdenticalPairs(nums))   









