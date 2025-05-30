class Solution(object):
    def Majoroity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output={}
        for i in nums:
            if i in output:
                output[i]+=1
            else:
                output[i]=1

        return max(output, key=output.get)
           

nums = [10,4,8,3,1,4,3,6,4]
solution = Solution()
print(solution.Majoroity(nums))