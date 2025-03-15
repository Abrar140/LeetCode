class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        maxScore=0
        maxScorenumber=0
        for i in range(len(divisors)):
            score=0
            for j in range(len(nums)):
                if nums[j]%divisors[i]==0:
                    score=score+1
            if score>maxScore:
                maxScore=score
                maxScorenumber=divisors[i]
            if score==maxScore and divisors[i]<maxScorenumber:
                maxScorenumber=divisors[i]
        if maxScore==0:
            return  min(divisors)
        return maxScorenumber




nums = [1]
divisors = [5,7,5]
solution = Solution()
print(solution.maxDivScore(nums, divisors))