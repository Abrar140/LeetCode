class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        dp=[0]*(n+1)
        print(dp)
        dp[1]=1 
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]


    
        

n = 4
instance = Solution()
print(instance.climbStairs(n))

