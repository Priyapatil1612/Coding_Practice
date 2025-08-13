class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # str_re = str(digits[0])
        # for i in range(1,len(digits)):
        #     temp = str(digits[i])
        #     str_re += temp
        # int_num = int(str_re)
        # int_num = int_num + 1
        # return[int(j) for j in str(int_num)]

        num = int(''.join(str(i) for i in digits))
        num += 1
        return [int(d) for d in str(num)]















