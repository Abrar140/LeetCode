class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maxcount1=0
        maxcount0=0
        count1=0
        count0=0
        for letter in s:
            if letter=='1':
                count1=count1+1
                maxcount1=max(maxcount1, count1)
                count0=0
            elif letter== '0' :
               count0=count0+1
               maxcount0=max(maxcount0, count0)
               count1=0
        if maxcount1>maxcount0:
            return True
        else:
            return False
        
        