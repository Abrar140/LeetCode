class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum1= float('-inf')
        maximum2=float('-inf')
        maximum3=float('-inf')
        for x in nums:
            if  x >maximum1:
                maximum3= maximum2
                maximum2= maximum1
                maximum1=x
            elif x>maximum2 and x!=maximum1:
                maximum3=maximum2
                maximum2=x
            elif x>maximum3 and x!=maximum1 and x!=maximum2:
                maximum3=x
        if maximum3==float('-inf'):
            return maximum1
        return maximum3

nums = [1,2]
s=Solution()
print(s.thirdMax(nums))