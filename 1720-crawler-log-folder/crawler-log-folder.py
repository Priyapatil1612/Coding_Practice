class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps_req = 0
        for i in logs:
            if i == '../':
                if steps_req>0:
                    steps_req -= 1
            elif i != './':
                steps_req +=1
        return steps_req