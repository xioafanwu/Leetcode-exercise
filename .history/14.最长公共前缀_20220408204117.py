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
        if len(x0)>0:
            for j in range(1,len(x0)):
                for i,x in enumerate(strs):
                    if x0[:j] in x:
                        continue
                    if (i==1)&(x0[:j] not in x):
                        return ""
                    if (i!=1)&(x0[:j] not in x):
                        return x0[:j-1]
        else:
            return ""

# @lc code=end

