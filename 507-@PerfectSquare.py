class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if  num <=1:
            return False
        sum=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sum+=i
                print(i, sum)
                if i != num // i:  # Avoid adding the square root twice for perfect squares.
                   sum += num // i

        return sum == num

       
      



# Example usage
num = 28
instance = Solution()
print(instance.checkPerfectNumber(num))