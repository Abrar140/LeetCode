class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing1=False
        decreasing=False
        increasing2=False
        for i in range(len(nums)-1):
                if nums[i]==nums[i+1]:
                    return False
            
                if increasing1== False:
                    if nums[i]<nums[i+1]:
                     increasing1=True
                    if nums[i]>nums[i+1]:
                      return False
                if increasing1==True:
                  
                   if nums[i]>nums[i+1]:
                    decreasing=True

                   if decreasing==True:
                      if nums[i]<nums[i+1]:
                        increasing2=True
                      if increasing2==True:
                        if(nums[i]> nums[i+1]):
                            return False
        if increasing1==True and decreasing==True and increasing2==True:
            return True
        else:
            return False



nums = [8,9,4,6,1]
solution=Solution()
solution.isTrionic(nums)
        

        
