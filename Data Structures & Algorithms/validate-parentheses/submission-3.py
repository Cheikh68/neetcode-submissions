class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack:
                    match char:
                        case ')':
                            if stack.pop() != '(':
                                return False
                        case '}':
                            if stack.pop() != '{':
                                return False
                        case ']':
                            if stack.pop() != '[':
                                return False
                else:
                    return False

        return not stack