class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        output={}
        outputlist=[]
        for i in range(len(nums1)):
            if nums1[i][0] in output:
                output[nums1[i][0]]+=nums1[i][1]
            else:
                output[nums1[i][0]]=nums1[i][1]

        for i in range(len(nums2)):
            if nums2[i][0] in output:
                output[nums2[i][0]]+=nums2[i][1]
            else:
                output[nums2[i][0]]=nums2[i][1]

        for key, value  in output.items():
            outputlist.append([key, value])
            
        outputlist.sort()
        
        return outputlist
        # nums1=nums1+nums2
      



nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[2,9],[3,2],[4,1]]

instance = Solution()
print(instance.mergeArrays(nums1,nums2))