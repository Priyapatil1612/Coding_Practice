class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
        # num = str(num)
        # ans = []
        # for i in num:
        #     if i == '6':
        #         ans.append(9)
        #     else:
        #         ans.append(int(i))
        # print()
