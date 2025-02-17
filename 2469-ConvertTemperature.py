class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        return [celsius + 273.15, celsius * 1.80 + 32.00]
        


celsius = 36.50
solution = Solution()
print(solution.convertTemperature(celsius))