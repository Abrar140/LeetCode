class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        outputmap={}
        for i in nums:
            if i in outputmap:
                outputmap[i]=outputmap[i]+1
            else:
                outputmap[i]=1

        keys = list(outputmap.keys())


        for i in range(len(keys) - 1):  
          for j in range(i + 1, len(keys)):  # j starts from i+1
             if outputmap[keys[i]] > outputmap[keys[j]] or (outputmap[keys[i]] == outputmap[keys[j]] and keys[i] < keys[j]):
                 keys[i], keys[j] = keys[j], keys[i]
                    
        outputarray=[]

        for key in keys:
            outputarray.extend([key]*outputmap[key])

        return outputarray


        


nums=[2,3,1,3,2]
sol=Solution()
print(sol.frequencySort(nums))










from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        freq = Counter(nums)  # O(n) to count frequencies
        return sorted(nums, key=lambda x: (freq[x], -x))  # O(n log n) sorting

# Test Case
nums = [1, 1, 2, 2, 2, 3]
sol = Solution()
print(sol.frequencySort(nums))  # Output: [3, 1, 1, 2, 2, 2] 