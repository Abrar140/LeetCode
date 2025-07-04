class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        prod=1
        flag=False
        if n<0:
            flag=True

        for i in range(0, abs(n)):
            prod=prod*x
        return flag and 1/prod or prod
        

x = 2.00000
n = -2
print(Solution().myPow(x, n))