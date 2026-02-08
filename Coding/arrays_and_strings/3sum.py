class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dictionary = {}
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left<right:
                sump = nums[left]+nums[right]
                if sump == -nums[i]:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sump > -nums[i]:
                    right -= 1
                else:
                    left += 1
        return res

                