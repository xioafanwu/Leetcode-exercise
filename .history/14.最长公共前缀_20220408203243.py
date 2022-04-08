#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        strs=['abc','abdfw','abui']
        x0=strs[0]
        j=1
        for i,x in enumerate(strs):
            if x0[:j] in x:
                j+=1
                continue
            else:
                return ""

# @lc code=end

