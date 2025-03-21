class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==2:
            return True
        
        count=0
        i=0
        n=len(nums)

        while i<n:
            if i+1==n:
                break
            if nums[i]==nums[i+1]:
                count=count+1
            if nums[i]>nums[i+1]:
                count=count+1
            print(nums[i])

            i=i+1
        
        if count==1 or count==0:
            return True
        return False
            

        
        
        
        i,  n =0, len(nums)
        while i+1<n and nums[i]<nums[i+1]:
            i+=1
        
        if i==n-1:
            return True
        
        
        print(nums, i)

        nums.pop(i)
        if i!=0:
            i-=1
        
        print(nums)
    
        
        while i+1<n-1 and nums[i]<nums[i+1]:
            i+=1
        
        if i==n-2:
            return True
        return False
        

        


nums = [2,3,1,2]
solution = Solution()
print(solution.canBeIncreasing(nums))