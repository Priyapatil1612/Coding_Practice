class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_emp = (i == 0) or (flowerbed[i-1] == 0)
                right_emp = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if left_emp and right_emp:
                    flowerbed[i] = 1
                    cnt += 1
        if cnt >= n:
            return True
        else:
            return False

