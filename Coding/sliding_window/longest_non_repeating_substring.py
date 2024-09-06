"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha_map = {}
        max_len = 0
        l = 0
        r = 0
        while r<len(s):
            if s[r] in alpha_map:
                while s[r] in alpha_map:
                    alpha_map.pop(s[l])
                    l+=1
                    
            else:
                max_len = max(max_len, r-l+1)
            alpha_map[s[r]] = 1 
            r+=1         
        return max_len

