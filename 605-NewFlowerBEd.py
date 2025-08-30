
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if flowerbed.count(0)<n:
            return False
        if n<=0:
            return True
        print("flowerbed", flowerbed, n, len (flowerbed))
        for flower in range(len(flowerbed)):
            left= flower-1
            right= flower+1
            if left<0:
                if right>=len(flowerbed):
                    if flowerbed[flower] == 0:
                          n -= 1
                          flowerbed[flower] = 1
                    if n == 0:
                        return True
                elif flowerbed[flower] == 0 and flowerbed[right] == 0:
                    n -= 1
                    flowerbed[flower] = 1
                    if n == 0:
                        return True
            elif right >= len(flowerbed):
                if flowerbed[flower] == 0 and flowerbed[left] == 0:
                    n -= 1
                    flowerbed[flower] = 1
                    if n == 0:
                        return True
            else:
                if  flowerbed[left] == 0 and flowerbed[flower] == 0 and flowerbed[right] == 0:
                    n -= 1
                    flowerbed[flower] = 1
                    if n == 0:
                        return True

        return False
                
          
        

# flowerbed =[1,0,0,0,0,1]
# n = 2

flowerbed =[1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1]
n = 209


solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))