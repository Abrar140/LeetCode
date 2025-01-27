class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """     
        buff=[]
        last=0
        for i in s:
            if last>0:
             if i.lower()==buff[last-1].lower() and i!=buff[last-1] :
                buff.pop()
                last-=1
             else:
                buff.append(i)
                last+=1
            else:
                buff.append(i)
                last+=1
        outputstring=[item for item in buff if item is not None]
        return "".join(outputstring)
s = "leEeetcode"
instance = Solution()
print(instance.makeGood(s))