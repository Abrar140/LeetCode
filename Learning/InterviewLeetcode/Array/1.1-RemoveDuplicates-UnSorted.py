class Solution(object):
    def removeDuplicates(self, nums):
        output={}
        current=0
        while current<len(nums):
            # print(nums[current+1],output)
            if nums[current]  in output:
                nums.pop(current)
            else:
                output[nums[current]]=1
                current=current+1 
             
        return nums



nums=[1,2,2,3,4,3,4,3,2,2,2,1,10]
solution=Solution()
print(solution.removeDuplicates(nums))