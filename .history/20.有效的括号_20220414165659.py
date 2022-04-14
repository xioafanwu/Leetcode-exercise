#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:

    def isValid( self,s):
        t=s.find('(')
        b=s.find('[')
        c=s.find('{')
        if (t!=-1):
            t1=s.find(')')
            if (t1!=-1)&((t1-t+1)%2==0):
                return True
        if (b!=-1):
            b1=s.find(']')
            if (b1!=-1)&((b1-b+1)%2==0):
                return True
        if (c!=-1):
            c1=s.find('}')
            if (c1!=-1)&((c1-c+1)%2==0):
                return True
        else:
            return False
# @lc code=end

s="){"

ou=isValid(s)