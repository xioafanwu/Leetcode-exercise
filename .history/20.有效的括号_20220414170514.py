#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:

    def isValid( self,s):
        new_str = ""
        def asb(s):
            t=s.find('(')
            b=s.find('[')
            c=s.find('{')
            if (t!=-1):
                t1=s.find(')')
                if (t1!=-1)&((t1-t+1)%2==0):
                    return True
                else:
                    return False
            if (b!=-1):
                b1=s.find(']')
                if (b1!=-1)&((b1-b+1)%2==0):
                    return True
                else:
                    return False
            if (c!=-1):
                c1=s.find('}')
                if (c1!=-1)&((c1-c+1)%2==0):
                    for i in range(0, len(s)):
                        if i != c:
                            new_str = new_str + s[i]
                        new_str1=''
                    for i in range(0, len(new_str)):
                        if i != c1-1:
                            new_str1 = new_str1 + new_str[i]                        
                    return True
                else:
                    return False
            else:
                return False
        
# @lc code=end

s="(){}}{"

ou=isValid(s)