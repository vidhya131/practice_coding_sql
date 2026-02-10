class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        m = {}
        res = 0
        while(right<n):    
            # move right
            if s[right] in m:
                if m[s[right]] >= left:
                    res = max(res, right-left)
                    left = m[s[right]]+1
            m[s[right]] = right
            right += 1
        res = max(res, right-left)
        
        return res
