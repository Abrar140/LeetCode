class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisblebynum=0
        nondivisiblebynum=0
        for i in range(1,n+1):
            if i%m==0:
                divisblebynum+=i
            else:
                nondivisiblebynum+=i
        return nondivisiblebynum-divisblebynum

n=10
m=3
sol=Solution()
print(sol.differenceOfSums(n,m))