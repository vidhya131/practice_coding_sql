class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for ind, val in enumerate(strs):
            count = [0]*26
            for j in val:
                count[ord(j) - ord("a")] += 1
            m[tuple(count)].append(val)

        return list(m.values())