class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        nums1= set(nums1)
        nums2= set(nums2)
        nums3= set(nums3)
        result = set()
        for num in nums1:
            if num in nums2 or num in nums3:
                result.add(num)
        for num in nums2:
            if num in nums1 or num in nums3:
                result.add(num)
        for num in nums3:   
            if num in nums1 or num in nums2:
                result.add(num)
        return list(result)
        

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(Solution().twoOutOfThree(nums1, nums2, nums3))