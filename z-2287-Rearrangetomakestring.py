class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        outputarray=[]
        for i in s:
            if i in target:
                outputarray.append(i)
        
        if len(s)<len(target):
            return 0
        print(outputarray)
        
        # while len(outputarray)>0:
        #     if outputarray[0] in target:



        output={}

        for i in s:
          if i in target:
            if i in output:
                output[i]+=1
            else:
                output[i]=1
        if output=={}:
            return 0
        
        print(output)

        if len(s)==min(output.values()):
            return 1
        return min(output.values())
       
       

      
        

s = "ilovecodingonleetcode"
target = "code"

instance = Solution()
print(instance.rearrangeCharacters(s, target))