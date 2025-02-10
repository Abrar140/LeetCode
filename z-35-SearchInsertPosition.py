class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
     
       
        return left
        #print(nums[mid], nums[left], nums[right])# mid==right=1, left=3
        print(nums[mid], nums[left], nums[right])# mid==left=10, right=8


nums = [1,3,5,8,10]
target = 9
Solution=Solution()
print(Solution.searchInsert(nums, target))