class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        outputarray=[]
        for x in range (1, n+1):
            if x%3==0 and x%5==0:
                outputarray.append("FizzBuzz")
            elif x%3==0:
                outputarray.append("Fizz")
            elif x%5==0:
                outputarray.append("Buzz")
            else:
                outputarray.append(str(x))
        return outputarray
                 





n=15
instance = Solution()
print(instance.fizzBuzz(n))  