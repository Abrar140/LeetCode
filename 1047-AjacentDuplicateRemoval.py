class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        buf=[]
        for i in s:
            if len(buf) == 0 :
                buf.append(i)
                last=i
            else:
                if i==last:
                    buf.pop()
                    if(len(buf)!=0):
                      last=buf[len(buf)-1]

                else:
                    buf.append(i)
                    last = i

        return "".join(buf)
           



s = "abbacja"
sol=Solution()
print(sol.removeDuplicates(s))