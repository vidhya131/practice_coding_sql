class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for i in nums_set:
            if i-1 not in nums_set:
                inc = 0
                while inc+i in nums_set:
                    inc += 1
                max_len = max(inc, max_len)
        return max_len