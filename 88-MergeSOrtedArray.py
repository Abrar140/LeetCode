class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p=len(nums1)-1
        while p>0 and m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[p]=nums1[m-1]
                m=m-1
            else:
                nums1[p]=nums2[n-1]
                n=n-1
            p=p-1
        while n>0:
            nums1[p]=nums2[n-1]
            n=n-1
            p=p-1
        print(nums1, nums2)
       

nums1 = [0]
m = 0
nums2 = [1]
n = 1

instance = Solution()
print(instance.merge(nums1, m, nums2, n))