#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        x0=strs[0]
        j=1
        for i,x in enumerate(strs):
            if x0[:j] in x:
                j+=1
                continue
            if (j==1)&(x0[:j] not in x):
                return ""
        return x0[:j]

# @lc code=end

