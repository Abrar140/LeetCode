class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        powerof3=[]
        for i in range(0,17):
            powerof3.append(3**i)
        for i in range(len(powerof3)):
            print(powerof3[i], i)

            m=n-powerof3[i]
            if m in powerof3:
                if m!=powerof3[i]:
                    return True
            m=0  
        return False


n=91
instance = Solution()
print(instance.checkPowersOfThree(n))

