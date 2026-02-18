class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        list=[]
        list[0]+list[1]==area
        list[0]>=list[1]
        # list[0]-list[1] minmum
        return list


area=4
print(Solution().constructRectangle(area))