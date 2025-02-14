class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operate_count = 0
        while nums[0] < k:
            if len(nums) < 2:
                return -1

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_ele = (min(x,y)*2 + max(x,y))
            heapq.heappush(nums,new_ele)

            operate_count += 1
        return operate_count

        