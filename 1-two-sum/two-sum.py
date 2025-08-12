class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BRUTCE FORCE
    
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        hmap ={}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in hmap:
                return [hmap[diff], index]
            hmap[val] = index