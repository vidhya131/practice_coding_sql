class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # declarations
        n = len(t)
        m = len(s)
        if m<n:
            return ""
        m1 = {}
        for i in range(n):
            m1[t[i]] = m1.get(t[i], 0)+1
        l = 0
        m2 = {}
        min_win = m+1
        min_substring = ""

        # logic
        for i in range(n-1):
            m2[s[i]] = m2.get(s[i], 0)+1
        r = n-1
        while(l<=r and r<m and (r-l+1)>= n):
            m2[s[r]] = m2.get(s[r], 0)+1
            # move the left pointer towards right pointer
            char = None
            while self.match(m1, m2, char):
                if min_win>r-l+1:
                    min_win = r-l+1
                    min_substring = s[l:r+1]
                m2[s[l]] = m2.get(s[l])-1
                if m2[s[l]] == 0:
                    del m2[s[l]]
                l += 1
            # move towards right
            r = r+1
        return min_substring


    def match(self, m1, m2, char):
        if char is not None:
            m2[char] = m2.get(char, 0) + 1
            for key, value in m1.items():
                if m2.get(key, 0) < value:
                    return False
            return True
        else:
            for key, value in m1.items():
                if m2.get(key, 0) < value:
                    return False
            return True
