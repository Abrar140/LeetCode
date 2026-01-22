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
        i=0
        j=0
        
        for z in range(length//2):
            if i<len(nums1):
                if nums1[i]>nums2[j]:
                    j=j+1
                else:
                    i=i+1
            if j<len(nums2):
                if nums1[i]>nums2[j]:
                    i=i+1
                else:
                    j=j+1

                print("i am abrar", nums1[i], nums2[j])
        if (length%2==0):
            print("i am here", nums1[i], nums2[j])
            return (float(nums1[i]+nums2[j])/2)
        else:
            if len(nums1)>len(nums2):
                return nums2[j]
            else:
                return nums1[i]
            

        #     print("i am here", nums1[i], nums2[j])
        
                

        # nums1=nums1+nums2

        # nums1.sort()
        # print("i am sort", nums1)
        # if len(nums1)%2==0:
        #     return float((nums1[len(nums1)//2] + nums1[(len(nums1)//2)-1])/2)
        # else:
        #     return nums1[len(nums1)//2]



# Example usage
nums1 = [1]
nums2 = [8,9]
instance = Solution()
print(instance.findMedianSortedArrays(nums1,nums2))  
