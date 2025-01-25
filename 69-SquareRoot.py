class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        for i in range(1, x//2+1):
            if i*i==x:
                return i

x=4
s=Solution()
print(s.mySqrt(x))