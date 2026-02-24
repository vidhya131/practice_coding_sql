class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        countT, window = {}, {}
        for i in range(n):
            countT[t[i]] = countT.get(t[i], 0) + 1
        min_win, min_substring = m + 1, [-1,-1]
        l, have, need = 0, 0, len(countT)
        for r in range(m):
            c = s[r]
            if c in countT:
                window[c] = window.get(c, 0)+1
                if window[c] == countT[c]:
                    have += 1
                while have == need:
                    if min_win > r-l+1:
                        min_win = r-l+1
                        min_substring = [l,r]
                    # remove the left chars to make the substr minimum
                    if s[l] in countT:
                        window[s[l]] -= 1
                        if countT[s[l]] > window[s[l]]:
                            have -= 1
                    l += 1

        return s[min_substring[0]:min_substring[1]+1]

                    

            