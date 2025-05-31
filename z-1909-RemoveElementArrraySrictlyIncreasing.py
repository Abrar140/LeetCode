class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==2:
            return True
        
     
        i=len(nums)-1
        n=len(nums)

        while i>0:
            print(i,"i")
            if i >= len(nums):  # <-- this avoids out of range
               i -= 1
               continue
            if nums[i-1]==nums[i] or nums[i-1]>nums[i]:
                print(i,".....1",nums[i-1],nums[i])
                if nums[i-2]==nums[i]:
                    print("i amhere")
                    nums.pop(i-2)
                elif nums[i-2]>nums[i]:
                    nums.pop(i)
                else:
                 nums.pop(i-1)
            else:
                i=i-1
            print("i  amnums",nums)

        if len(nums)==n-1 or len(nums)==n:
            return True
        return False
            
        

nums = [100,21,100]
solution = Solution()
print(solution.canBeIncreasing(nums))