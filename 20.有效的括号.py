#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or stack[-1]!=i:
                return False
            else:
                stack.pop()
        return True if not stack else False
# @lc code=end