class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0]*n
        stack = []
        for i in range(n):
            while stack and temp[stack[-1]]<temp[i]:
                top = stack.pop()
                res[top] = i-top
                
            stack.append(i)
        return res