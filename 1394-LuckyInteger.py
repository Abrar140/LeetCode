class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        output={}
        max=-1
        for i in arr:
            if i in output:
                output[i]+=1
            else:
                output[i]=1
        for key, value in output.items():
            if key==value:
                if value>max:
                    max=value

        return  max
        print(output)
        


arr = [2,2,3,4, 4,4,4]
print(Solution().findLucky(arr))