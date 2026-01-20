class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        # Start from the end
        p1 = m - 1  # Pointer for nums1 (valid part)
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # End of nums1

        print(p1, p2, p)

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1

            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            print(p1, p2, p,nums1)

        # If any elements left in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        # No need to copy from nums1; they are already in place

# Example usage
nums1 = [1, 2, 10, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 2, 5, 6]
