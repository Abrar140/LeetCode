class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        output={}
        for i in deck:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1
        min_count = min(output.values())
        for i in output.values():
            print(i, min_count)
            if i < 2 or i % min_count != 0:
                for j in range(2, min_count + 1):
                    print(i, j, min_count)
                    if  i % j == 0 and min_count % j == 0:
                        continue
                        continue
                      
                return False
 
        return True
       



    
deck=[1,1,1,1,2,2,2,2,2,2]
print(Solution().hasGroupsSizeX(deck))
