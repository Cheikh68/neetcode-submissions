class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case '+':
                    value = stack.pop() + stack.pop()
                    stack.append(value)
                case '-':
                    value = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(value)
                case '*':
                    value = stack.pop() * stack.pop()
                    stack.append(value)
                case '/':
                    value = stack[-2] / stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(value))
                case _:
                    stack.append(int(token))
        
        return stack[0]