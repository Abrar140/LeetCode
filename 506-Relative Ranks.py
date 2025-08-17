class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        newsorted = sorted(score, reverse=True)
        output={}
        for i in range(len(score)):
            if score[i] == newsorted[0]:
                output[score[i]] = "Gold Medal"
            elif score[i] == newsorted[1]:
                output[score[i]] = "Silver Medal"
            elif score[i] == newsorted[2]:
                output[score[i]] = "Bronze Medal"
            else:
                output[score[i]] = str( newsorted.index(score[i]) + 1)

        return [output[i] for i in score]


score = [10,3,8,9,4]
print(Solution().findRelativeRanks(score))