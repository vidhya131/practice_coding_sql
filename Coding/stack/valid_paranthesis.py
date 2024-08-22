"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

# solution

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == ']' and self.top(st) == '[':
                self.pop(st)
            elif i == '}' and self.top(st) == '{':
                self.pop(st)
            elif i == ')' and self.top(st) == '(':
                self.pop(st)
            else:
                self.push(st,i)

        if self.top(st): 
            return False
        else:
            return True

    def push(self, stack, element):
        print(element)
        top = len(stack)-1
        stack.append(element)

    def pop(self, stack):
        stack.pop(-1)

    def top(self, stack):
        if len(stack):
            top_element = stack[-1]
            return top_element
        else:
            return False
        