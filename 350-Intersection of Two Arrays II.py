class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        output = []
        for i in nums1:
            if i in nums2:
                output.append(i)
                nums2.remove(i)
        return output



nums1 = [1,2,2,1]
nums2 = [2,2]
sol=Solution()
print(sol.intersect(nums1, nums2))