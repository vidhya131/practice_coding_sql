class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        n = len(nums)
        for i in range(n):
            if target - nums[i] in m:
                return [i, m[target - nums[i]]]
            m[nums[i]] = i
        return []

