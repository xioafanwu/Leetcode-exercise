#
# @lc app=leetcode.cn id=541 lang=python3
# @lcpr version=30201
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0,len(s),k*2):
            s[i:i+k]=s[i:i+k][::-1]
        return ''.join(s)
# @lc code=end



#
# @lcpr case=start
# "abcdefg"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

#

