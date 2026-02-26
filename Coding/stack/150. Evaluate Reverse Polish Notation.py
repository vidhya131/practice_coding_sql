class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        lis = ['+', '-', '/', '*']
        for token in tokens:
            if token not in lis:
                stack.append(token)
            else:
                el1 = int(stack.pop())
                el2 = int(stack.pop())
                res = el2
                if token == '+':
                    res += el1
                elif token == '-':
                    res -= el1
                elif token == '/':
                    res /= el1
                elif token == '*':
                    res *= el1

                stack.append(res)
        return int(stack.pop())
