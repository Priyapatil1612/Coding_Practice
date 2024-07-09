class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        total_wait_time = 0

        for arrival, wait_time in customers:
            if time > arrival:
                total_wait_time += time - arrival
            else:
                time = arrival
            total_wait_time += wait_time
            time += wait_time
        return total_wait_time/len(customers)