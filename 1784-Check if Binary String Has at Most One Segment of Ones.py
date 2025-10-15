class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=='1':
         return True
        count1=0
        count0=0
        for letter in s:
            if letter=='1':
                if count0>=1:
                    return False
                count1=count1+1
                count0=0
            if letter=='0':
                count0=count0+1
                # count1=0
                
        if s.count('1')==count1:
            return True
        else:
            return False

        