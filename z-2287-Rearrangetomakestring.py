class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        output={}
        if len(s)<len(target):
            return 0
        for i in s:
          if i in target:
            if i in output:
                output[i]+=1
            else:
                output[i]=1
        # print(output, )
        if len(s)==min(output.values()):
            return 1
        return min(output.values())
       
       

        # for i in target:
        #     if i in output:
        #         outputnumber+=output[i]//2
        #     else:
        #         return 0
        # return outputnumber
        

s = "abbaccaddaeea"
target = "aaaaa"

instance = Solution()
print(instance.rearrangeCharacters(s, target))