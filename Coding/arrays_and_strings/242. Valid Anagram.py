class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        if len(s) != len(t):
            return False

        for _,val in enumerate(s):
            m[val] = 1+m.get(val, 0)

        for _, val in enumerate(t):
            count = m.get(val, 0)
            if count == 0:
                return False
            else:
                m[val] -= 1
            if m[val]<0:
                return False
        return True


        # other approach to not to use space complexity - sorting


        