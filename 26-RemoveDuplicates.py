class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=0
        while current<len(nums):
            if current==len(nums)-1:
                break
            if nums[current]==nums[current+1]:

                nums.pop(current+1)
            else:
                current=current+1
        return (len(nums))



nums=[0,0,1,1,1,1,2,3,3]
instance=Solution()
print(instance.removeDuplicates(nums))