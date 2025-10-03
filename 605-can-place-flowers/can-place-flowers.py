class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        length=len(flowerbed)

        for i in range (length):
            if flowerbed[i] ==0:
                empty_left=(i==0 or flowerbed[i-1]==0)
                empty_right=(i==length-1 or flowerbed[i+1] ==0)
                if (empty_right and empty_left):
                    flowerbed[i]=1
                    count+=1
        return count>=n

        