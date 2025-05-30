class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1=nums1+nums2
        print(nums1)
        
        for i  in range(len(nums1)-1):
            print(i,nums1[i])
            if nums1[i]==0:
                nums1.pop(nums1[i])

        print("we are here",nums1)
        pointer1=0
        pointer2=0
      
        for i in range(m,m+n):
            print(i,m,n)
            # nums1[i]=nums2[]

        while pointer1<m and pointer2<n:
            if nums1[pointer1]>=nums2[pointer2]:
                nums1[m+pointer2]=nums1[pointer1]
                pointer1+=1
            else:
                nums1[m+pointer2]=nums2[pointer2]
                pointer2+=1

        nums1.sort()

        print(nums1)
        #     if nums1[pointer1]>nums2[pointer2]:
        #         nums1[m+pointer2]=nums1[pointer1]
        #         pointer1+=1
        #     else:
        #         nums1[m+pointer2]=nums2[pointer2]
        #         pointer2+=1

        # while pointer1<m:
        #     nums1[m+pointer2]=nums1[pointer1]
        #     pointer1+=1
        # while pointer2<n:
        #     nums1[m+pointer2]=nums2[pointer2]
        #     pointer2+=1
    

nums1 = [1,2,2,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

instance = Solution()
print(instance.merge(nums1, m, nums2, n))