class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        peak=[]
        for i in range (1, len(mountain)-1):
            if mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]:
                peak.append(i)
        return peak



mountain = [1,4,3,8,5]
print(Solution().findPeaks(mountain))