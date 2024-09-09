"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
"""
#  solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l = l+1
                    r = r-1
                    while l<r and nums[l]==nums[l-1]:
                        l = l+1
                    while l<r and nums[r]==nums[r+1]:
                        r = r-1

                elif sum<0:
                    l = l+1
                else:
                    r = r-1
        return res
