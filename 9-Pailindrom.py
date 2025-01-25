class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x= str(x)
        for i in range (len(x)//2):
            if x[i]!= x[len(x)-i-1]:
             return False
        return True

        
       



x= 0
instance = Solution()
print(instance.isPalindrome(x))