class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i  in  range(len(nums)):
            print(i,(i+k)%len(nums),nums[i],nums[(i+k)%len(nums)])
            nums[i],nums[(i+k)%len(nums)-1]=nums[(i+k)%len(nums)-1],nums[i]
            print(nums)
    
            # print(i)
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
sol=Solution()
print(sol.rotate(nums,k))