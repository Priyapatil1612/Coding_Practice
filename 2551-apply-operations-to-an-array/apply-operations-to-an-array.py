class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        non_zero=[n for n in nums if n!= 0]
        zeros = [0]*(len(nums)-len(non_zero))
        return non_zero + zeros