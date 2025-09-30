class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ## dp approach
        
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        res = s[0]
        for i in range(n-2, -1, -1):
            for j in range(n-1, 0, -1):

                if s[i] == s[j]:
                    if dp[i+1][j-1]==1 or j-i==1:
                        if len(res)<j-i+1:
                            res = s[i:j+1]
                        dp[i][j] = 1
        # print(dp)
        return res

        ## non-dp approach
        """
        res=""
        reslen=0
        for i in range(n):
            l,r=i,i
            while(l>=0 and r<n and s[l]==s[r]):
                if r-l+1>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            while(l>=0 and r<n and s[l]==s[r]):
                if r-l+1>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
        return res
        """
