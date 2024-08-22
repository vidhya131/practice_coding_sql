"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

# solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for c in s:
            asc_ch = ord(c)
            if (asc_ch>=65 and asc_ch<=90) or (asc_ch>=97 and asc_ch<=122) or (asc_ch>=48 and asc_ch<=57):
                s1 += str(c)
        l = 0
        r = len(s1)-1
        while(l<r):
            if s1[l].lower()!=s1[r].lower():
                return False
            l += 1
            r -= 1
        return True
          