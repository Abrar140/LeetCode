# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         if n<=0:
#             return True
#         for flower in range(len(flowerbed)):
#             if  flowerbed[flower] == 0:
#                 if (flower==0 and flowerbed[flower+1] == 0) or (flower==len(flowerbed)-1 and flowerbed[flower-1] == 0):
#                     n -= 1
#                     flowerbed[flower] = 1
#                     if n == 0:
#                         return True
#                 elif flowerbed[flower-1] == 0 and flowerbed[flower+1] == 0:
#                  n -= 1
#                  flowerbed[flower] = 1
#                  if n == 0:
#                     return True
                
#         return False
#             # print(flower)
#             # print("jjjjj", flowerbed[flowerbed.index(flower)-1])
#             # if flower == 0   and  flowerbed[flowerbed.index(flower)-1] == 0 and flowerbed[flowerbed.index(flower)+1] == 0:
#             #     n -= 1
#             #     if n == 0:
#             #         return True
        

# flowerbed = [0]
# n = 1

# solution = Solution()
# print(solution.canPlaceFlowers(flowerbed, n))











class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return True
        for flower in range(len(flowerbed)):
            if flowerbed[flower] == 1:
                continue
            if flower == 0   and  (flower-1 <0 or flower+1 > len(flowerbed)-1):
                return True
            if  flowerbed[flower] == 0 and flowerbed[flower-1] == 0 and flowerbed[flower+1] == 0:
                n -= 1
                flowerbed[flower] = 1
                if n == 0:
                    return True
            elif flowerbed[flower] == 0 and  (flower==0 and flowerbed[flower+1] == 0) or (flower==len(flowerbed)-1 and flowerbed[flower-1] == 0):
                    n -= 1
                    flowerbed[flower] = 1
                    if n == 0:
                        return True
            
                
        return False
            # print(flower)
            # print("jjjjj", flowerbed[flowerbed.index(flower)-1])
            # if flower == 0   and  flowerbed[flowerbed.index(flower)-1] == 0 and flowerbed[flowerbed.index(flower)+1] == 0:
            #     n -= 1
            #     if n == 0:
            #         return True
        

flowerbed = [0]
n = 1

solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))