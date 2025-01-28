class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        i = 0
        while i < len(nums1):
          if nums1[i] in nums2:
            nums2.remove(nums1[i])
            nums1.pop(i)
          else:
            i += 1
    
        return[ nums1, nums2]

nums1 = [-17,-6,8,-13,15,-16,16,-11,-10,-16,6,1,-12,-5,-1,-9,1]
nums2=[-16,-16,-14,-17,-5,-4,17,2,3,0,-2,4,16,-11,-6,-9,-15]

instance = Solution()
print(instance.findDifference(nums1,nums2))