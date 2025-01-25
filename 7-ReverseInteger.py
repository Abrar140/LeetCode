class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>-10 and x<10:
            return x
        strg = ""
        neg=False
        if x<0:
            neg =True
            x=abs(x)
        while x!=0:
            rev=x%10
            strg=strg+""+ str(rev)
            x=x//10
            
        if neg ==True:
            strg=int(strg)*-1 
            if  strg< -2**31:
                return 0
            else:
                return strg
        else:
            if  int(strg)> 2**31-1:
                return 0
            else:
                return  int(strg)
        



print(2**31-1)
x= -123450
instance = Solution()
print(instance.reverse(x))