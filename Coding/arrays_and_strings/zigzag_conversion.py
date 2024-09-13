"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

# solution

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        l = []
        # corner cases
        if n == 1:
            return s
        if n == 0:
            return '' 
           
        for i in range(n):
            l.append([])
        rownum = 0
        i = 0
        while i<len(s) and rownum<n:
            if rownum == 0: 
                l[rownum].append(s[i])
                rownum += 1
                i += 1
                while rownum<n and i<len(s): 
                    l[rownum].append(s[i])
                    rownum +=1
                    i+=1
                rownum = n-2
            else:
                l[rownum].append(s[i])
                i += 1
                rownum -= 1   
        res = ""      
        for i in l:
            for j in i:
                res += str(j)
        return res        
            
