class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output=[]
        includeinoutput=False
        for i in range(left, right+1):
            digits = list(set(int(d) for d in str(i)))  # Extract unique digits
            for digit in digits:
               if digit == 0: 
                    includeinoutput=True
                    break
               if i%digit != 0:
                        includeinoutput=True
                        break
                        

            if includeinoutput is False:
                output.append(i)

            includeinoutput=False




                    


        return output
            
        


left = 1
right = 22

print(Solution().selfDividingNumbers(left, right))