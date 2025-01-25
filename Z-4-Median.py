# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         nums1=nums1+nums2
#         nums1.sort()
#         if len(nums1)%2==0:

#             return float((nums1[len(nums1)//2] + nums1[(len(nums1)//2)-1])/2)
#         else:
#             return nums1[len(nums1)//2]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length=len(nums1)+len(nums2)
        print(length,length//2)
        nums1=nums1+nums2

        nums1.sort()
        if len(nums1)%2==0:
            return float((nums1[len(nums1)//2] + nums1[(len(nums1)//2)-1])/2)
        else:
            return nums1[len(nums1)//2]



# Example usage
nums1 = [1,2,8,12]
nums2 = [3,4]
instance = Solution()
print(instance.findMedianSortedArrays(nums1,nums2))  
