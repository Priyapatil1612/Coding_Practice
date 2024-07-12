class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(s, target, points):
            stack = []  # Initialize an empty stack
            score = 0
            for char in s:
                # Check if the top of the stack and the current character form the target substring
                if stack and stack[-1] + char == target:
                    stack.pop()  # Remove the top element from the stack
                    score += points  # Add points for the removal
                else:
                    stack.append(char)  # Push the current character onto the stack
            return ''.join(stack), score  # Return the modified string and the score
    
        if x > y:
            # Remove "ab" first
            s, score1 = remove_and_score(s, 'ab', x)
            _, score2 = remove_and_score(s, 'ba', y)
        else:
            # Remove "ba" first
            s, score1 = remove_and_score(s, 'ba', y)
            _, score2 = remove_and_score(s, 'ab', x)
        
        return score1 + score2

        # def give_score(s,target,points):
        #     stack1 = []
        #     score = 0
        #     for i in s:
        #         if stack1 and stack1[-1]+i == target:
        #             stack1.pop()
        #             score += points
        #         else:
        #             stack1.append(i)
        #     return score
        # if x > y :
        #     score1 = give_score(s,'ab',x)
        #     score2 = give_score(s,'ba',y)
        # else:
        #     score1 = give_score(s,'ba',y)
        #     score2 = give_score(s,'ab',x)
        # return score1+score2