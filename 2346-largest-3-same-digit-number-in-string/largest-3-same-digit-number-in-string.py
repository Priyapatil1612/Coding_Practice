class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                temp = num[i] * 3
                result = max(result,temp)
        return result
        # return max(temp,key=int) if temp else ""
                

         