class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for si in s:
            if si == ')':
                temp=[]
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                if stack: 
                    stack.pop()
                stack.extend(temp)
            else:
                stack.append(si)
        return ''.join(stack)

        