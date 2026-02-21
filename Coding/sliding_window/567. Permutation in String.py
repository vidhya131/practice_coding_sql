class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = {} 
        n = len(s1)
        m = len(s2)
        if m < n:
            return False
        for i in range(len(s1)):
            m1[s1[i]] = m1.get(s1[i], 0)+1

        st = 0
        end = n-1
        m2 = {}
        for i in range(n):
            m2[s2[i]] = m2.get(s2[i], 0)+1
        
        while(end<m):
            k = self.match(m1, m2)
            if k:
                return True

            # undo
            m2[s2[st]] = m2[s2[st]]-1
            if m2[s2[st]] == 0:
                del m2[s2[st]]
         
            # update
            st += 1
            end += 1
            if end < m:
                m2[s2[end]] = m2.get(s2[end], 0)+1



        return False
            
    def match(self, m1, m2):
        return m1 == m2

        # f1 = True
        # for key, val in m1.items():
        #     if (key not in m2) or (key in m2 and m2[key] != val):
        #         f1 = False
        #         break
        # return f1         

                 