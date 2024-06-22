#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack):
            if haystack[i:i+len(needle)] == needle:
                return i

length=[]
spac=[0]
for i in range(len(s)):
    if s[i]==' ':
        length.append(i-spac[-1])
        spac.append(i)
length=[i for i in length if i>1]

# @lc code=end

