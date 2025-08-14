class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        map={}

        for i in range(len(items1)):
            if items1[i][0] not in map:
                map[items1[i][0]] = items1[i][1]
            else:
                map[items1[i][0]] += items1[i][1]
        for i in range(len(items2)):
            if items2[i][0] not in map:
                map[items2[i][0]] = items2[i][1]
            else:
                map[items2[i][0]] += items2[i][1]

        map= dict(sorted(map.items()))
        return [[key, value] for key, value in map.items()]

        #     for j in range(len(items2)):
        #         if items1[i][0] == items2[j][0]:
        #             items1[i][1] += items2[j][1]
        #             break
        #         else:
        #             items1.append(items2[j])
        # items1.sort(key=lambda x: x[0])
        # return items1
       
            



items1 = [[28,3],[12,4],[29,8]]
items2 = [[28,6],[12,8],[29,9]]
print(Solution().mergeSimilarItems(items1, items2))