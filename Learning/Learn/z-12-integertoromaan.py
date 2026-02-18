class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        number=1
        stringnumber=""
        while num !=0:
            nums=num%10
            nums=nums*1
            if nums>10:
             print(nums)
            num=0

            
        print(num//10, num%10)
        print(num)
        return  str(num)

num=45
s=Solution()
print(s.intToRoman(num))