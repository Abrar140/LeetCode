class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m*n != len(original):
            return []
        result = []
        for  i in range(m):
            result.append([])
            for j in range(n):
                result[i].append(original[i*n+j])

        return result
        print(original, m, n, result)
        


original = [1,2,3,4]
m = 2
n = 2

solution = Solution()
print(solution.construct2DArray(original, m, n))










    #  if m * n != len(original):
    #         return []
    #     return [original[i:i+n] for i in range(0, len(original), n)]