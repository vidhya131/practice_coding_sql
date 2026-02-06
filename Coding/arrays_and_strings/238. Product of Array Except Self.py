class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n

        for i in range(1, n):
            prefix[i] = nums[i-1]*prefix[i-1]
        
        postfix = nums[n-1]
        for i in range(n-2, -1, -1):
            prefix[i] = prefix[i]*postfix
            postfix = postfix*nums[i]

        return prefix

                    