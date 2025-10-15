class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcount=0
        count1=0
        for num in nums:
            if num==1:
                count1=count1+1
            if num==0 :
                if count1>maxcount:
                    maxcount=count1
                count1=0
        if count1>maxcount:
                    maxcount=count1
        
        return maxcount



        