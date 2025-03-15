class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """

        # it work correctly for smaller inputs but not for large inputs it fails check Ai version




        
        num=""
        partionlist=[]
        for number in nums:
            if number!=",":
                num += str(number)
                partionlist.append(num)
        outputpartionlist=[]
        
        for eachnum in partionlist:
          decimalnumber=0
          power=0
          for digit in reversed(eachnum):
            decimalnumber+=int(digit)*2**power
            power+=1
          if decimalnumber%5==0:
            outputpartionlist.append(True)
          else:
            outputpartionlist.append(False)
        return outputpartionlist


nums=[0,1,1,1,1,1]
solution=Solution()
print(solution.prefixesDivBy5(nums))


















