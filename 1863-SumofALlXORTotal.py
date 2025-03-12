class Solution(object):
    def get_subsets(self,lst, index=0, current=[], result=None):
     if result is None:
        result = []
     if index == len(lst):
        result.append(current[:])  # Append a copy of current subset
        return
     self.get_subsets(lst, index + 1, current + [lst[index]], result)  # Include element
     self.get_subsets(lst, index + 1, current, result)  # Exclude element
     return result
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        allsubsets=self.get_subsets(nums)
        sum=0
        for set in allsubsets:
            xor=0
            for  element in set:
                xor=xor^element
            sum+=xor
            
        return sum
        


nums = [1,3]
solution = Solution()
print(solution.subsetXORSum(nums))