class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        Output=[]
        minindex= float('inf')
        for index in range(len(list1)):
            if list1[index] in list2:
                indexvalue= index+ list2.index(list1[index])
                if minindex==indexvalue:
                    Output.append(list1[index])
                elif minindex>indexvalue:
                    Output=[]
                    minindex=indexvalue
                    Output.append(list1[index])
        return Output

        