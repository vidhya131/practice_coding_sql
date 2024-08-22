"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

# solution

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # n = len(nums)
        # dp=[-1]*n
        # dp[0] = 1    
        # for i in range(0,n):
        #     if(dp[i] == 1):
        #         l=min(len(nums),i+nums[i]+1)
        #         for j in range(i, l):
        #             dp[j] = 1    
        # return dp[-1] == 1  
        last_position = 0
        for i in range(len(nums)):
            if i > last_position:
                return False
            last_position = max(last_position, i + nums[i])
            if last_position >= len(nums) - 1:
                return True      

