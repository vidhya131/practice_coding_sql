class Solution:
    def partitionString(self, s: str) -> int:
        ## why greedy works?
        latest = set() 
        c = 1 #(+1 for the last substring)
        for i in range(len(s)):
            if s[i] in latest:
                c += 1
                latest = set()
            latest.add(s[i])
        return c
        

