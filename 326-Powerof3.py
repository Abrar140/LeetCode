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




# class Solution(object):
#     def isPowerOfThree(self, n):
#         if n <= 0:
#             return False
        
#         while n % 3 == 0:
#             n = n // 3
        
#         return n == 1
