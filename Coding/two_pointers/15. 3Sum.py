class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        res = []
        print(nums)
        for i in range(n):
            # skip duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            # freeze i
            left = i+1
            right = n-1
            while left<right:
                sm = nums[left]+nums[right]
                target = -nums[i]
                if sm == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sm < target:
                    left += 1
                else:
                    right -= 1
        return res