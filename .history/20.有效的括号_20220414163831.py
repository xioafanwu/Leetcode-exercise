#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        t=s.find('(')
        b=s.find('[')
        c=s.find('{')
        if (t!=-1)&(s[t+1]!=')'):
            return False
        if (b!=-1)&(s[b+1]!=']'):
            return False
        if (c!=-1)&(s[c+1]!='}'):
            return False
        else:
            return True
# @lc code=end

