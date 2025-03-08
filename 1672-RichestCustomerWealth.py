class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # return max([sum(i) for i in accounts])
        maximum=0
        temp=0
        for i in accounts:
            temp=0
            for j in i:
                temp=temp+j
            if temp>maximum:
                maximum=temp

        return maximum
                

accounts = [[1,2,3],[3,2,1]]
print(Solution().maximumWealth(accounts))