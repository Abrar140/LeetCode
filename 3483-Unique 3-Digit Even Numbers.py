class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count = 0
        numberarray= set()
        
        for i in range(len(digits)):
         for j in range( len(digits)):
           for k in range( len(digits)):
                         if i != j and j != k and i != k:  # make sure digits are unique

                                 numberarray.add(digits[i]*100 + digits[j]*10 + digits[k])

        for number in numberarray:
            if number % 2 == 0   and number>= 100 and number <= 999:
                count += 1
        return count




digits = [1,2,3,4]
print(Solution().totalNumbers(digits))