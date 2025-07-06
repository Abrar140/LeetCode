class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        output=[]
        output.append(n)
        while n!=1:
            sum=0
            while n>0:
                sum+=((n%10)**2)
                n=n//10
            n=sum
            if n in output:
                return False
            output.append(n)
       
        return True
       
        

n = 19
instance = Solution()
print(instance.isHappy(n))