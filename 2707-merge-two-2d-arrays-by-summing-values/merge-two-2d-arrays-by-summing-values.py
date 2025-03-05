class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        my_dict = {}
        for i in nums1,nums2:
            for j in i:
                key = j[0]
                value = j[1]
                if key in my_dict:
                    my_dict[key] += value
                else:
                    my_dict[key] = value
        sorted_dict = dict(sorted(my_dict.items()))
        ans = []
        for k,v in sorted_dict.items():
            temp_li = [k,v]
            ans.append(temp_li)
        return ans