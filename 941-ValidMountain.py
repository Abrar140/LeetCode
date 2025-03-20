class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        
        maximum= max(arr)
        maximumindex=arr.index(maximum)

        if maximumindex==0 or maximumindex==len(arr)-1:
            return False
        
        for i in range(0, maximumindex):
            if arr[i]>=arr[i+1]:
                return False
        
        for i in range(maximumindex, len(arr)):
            if i==len(arr)-1:
                return True
            if arr[i]<=arr[i+1]:
                return False
        return True
        

        

        




arr = [3,5,5]
solution = Solution()
print(solution.validMountainArray(arr))