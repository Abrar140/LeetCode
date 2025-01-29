class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map={}
        for i in nums:
            if i in map:
               map[i] += 1
            else:
                map[i]=1
        return (max(map.keys(), key=map.get))

        print(map.keys())

        print(max(map.keys(), key=map.get))


nums = [3,3,4]
sol=Solution()
print(sol.majorityElement(nums))