class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=0
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                # if nums[i]>nums[i-1]:
                print(i, nums[i])
                continue
            else:
                current+=1
        return current
        # return len(set(nums))



nums=[0,0,1,1,1,1,2,3,3]
instance=Solution()
print(instance.removeDuplicates(nums))