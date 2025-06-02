class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subsets=[]
        output={}
        for  i in range(len(nums)):
            if i+k-1==len(nums):
                break
            subsets.append(set(nums[i:i+k]))

        for subset in subsets:
            for nums in subset:
                if nums not in output:
                    output[nums]=1
                else:
                    output[nums]+=1
      
        listy=[k for k, v in output.items() if v == 1]
      
        if listy:
            return max(listy)
        else:
            return -1
        print(listy)
      
        

sol=Solution()
nums = [0,0]
k = 2
print(sol.largestInteger(nums,k))