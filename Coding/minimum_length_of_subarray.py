"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

"""
 
# Solution:
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        r = 0
        cur_sum = nums[l]
        mini = len(nums)+1
        while l<=r and r<len(nums):
            print(l)
            print(r)
            if cur_sum >= target:
                mini = min(mini,r-l+1)
                cur_sum -= nums[l]
                l += 1
            elif cur_sum<target:
                r += 1
                if r<len(nums):
                    cur_sum += nums[r]    
        return  mini if mini != len(nums)+1 else 0
