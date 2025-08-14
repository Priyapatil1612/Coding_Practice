class Solution:
    def largestGoodInteger(self, num: str) -> str:
        temp = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                temp.append(str(num[i]) + str(num[i+1]) + str(num[i+2]))
        return max(temp,key=int) if temp else ""
                

         