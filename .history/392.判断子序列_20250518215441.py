#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30201
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n=0, 0
        result=0
        while n<len(t):
            if t[n]!=s[m]:
                n+=1
            if t[n]== s[m]:
                m+=1
                n+=1
                result+=1
        if result==len(s):
            return True
        else:
            return false
# @lc code=end



#
# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

#

