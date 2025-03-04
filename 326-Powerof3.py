class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        powerof3=[]
        for i in range(0,31):
            powerof3.append(3**i)

        if n in powerof3:
            return True
        return False
     


n=91
instance = Solution()
print(instance.isPowerOfThree(n))

