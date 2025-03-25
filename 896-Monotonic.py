class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start=0
        end=len(nums)
        maxi=max(nums)
        maxindex=nums.index(maxi)
        if maxi==nums[end-1]:
            while start<end:
                if start==end-1:
                    return True
                else:
                 if nums[start]<nums[start+1]:
                    start+=1
                 elif nums[start]>nums[start+1]:
                    return False
                 elif nums[start]==nums[start+1]:
                    start+=1

        elif maxi==nums[start]:
            while start<end:
                if start==end-1:
                    return True
                else:
                 if nums[start]>nums[start+1]:
                    start+=1
                 elif nums[start]<nums[start+1]:
                    return False
                 elif nums[start]==nums[start+1]:
                    start+=1
        else:
            return False
        # while start<end:


        
        # list=[-1,0,1]
        # number=0
        # for index, x in enumerate(nums):
        #     if index==len(nums)-1:
        #         return True
        #     number=nums[index]-nums[index+1]
        #     if number not in list:
        #         return False
        # return True

nums = [6,5,4,4]

instance = Solution()
print(instance.isMonotonic(nums))  