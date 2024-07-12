class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def give_score(s,target,points):
            stack1 = []
            score = 0
            for i in s:
                if stack1 and stack1[-1]+i == target:
                    stack1.pop()
                    score += points
                else:
                    stack1.append(i)
            return ''.join(stack1),score
        if x > y :
            s,score1 = give_score(s,'ab',x)
            _,score2 = give_score(s,'ba',y)
        else:
            s,score1 = give_score(s,'ba',y)
            _,score2 = give_score(s,'ab',x)
        return score1+score2