class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        outputmap={}
        for i in nums:
            if i in outputmap:
                outputmap[i]=outputmap[i]+1
            else:
                outputmap[i]=1

        for i in outputmap:
            # if outputmap[i]%2!=0:
                return False
        return True
        


nums = [3,2,3,2,2,2]
sol=Solution()
print(sol.divideArray)