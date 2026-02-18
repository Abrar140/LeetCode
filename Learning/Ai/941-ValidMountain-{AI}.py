class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False

        i, n = 0, len(arr)

        # Climb up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak can't be the first or last element
        if i == 0 or i == n - 1:
            return False

        # Climb down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1

# Example usage
arr = [3, 5, 5]
solution = Solution()
print(solution.validMountainArray(arr))
