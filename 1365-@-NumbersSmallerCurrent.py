class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # count=0
        # output=[]
        # for num in nums:
        #      count=0
        #      for small in nums:
        #         print(num,small,count)
        #         if num>small:
        #             count+=1
        #      output.append(count)

        # return output





        return [sum(x > y for y in nums) for x in nums]

nums = [8,1,2,2,3]
solution = Solution()
print(solution.smallerNumbersThanCurrent(nums))