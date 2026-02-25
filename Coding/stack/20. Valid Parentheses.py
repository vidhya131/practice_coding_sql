class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['{','(', '[']:
                stack.append(i)
            else:
                if stack:
                    top = stack.pop()
                else:
                    return False
                if i == '}' and top != '{':
                    return False
                if i == ']' and top != '[':
                    return False
                if i == ')' and top != '(':
                    return False
        return len(stack) == 0   


        