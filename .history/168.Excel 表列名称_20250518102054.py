#
# @lc app=leetcode.cn id=168 lang=python3
# @lcpr version=30201
#
# [168] Excel 表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        yushu=columnNumber
        s=''
        if columnNumber<=26:
            return chr(columnNumber + ord('A') - 1)
        else:
            while yushu>0:
                yushu=yushu-1
                num=yushu%26
                s=chr(num + ord('A'))+s
                yushu=yushu//26
            return s

# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 28\n
# @lcpr case=end

# @lcpr case=start
# 701\n
# @lcpr case=end

# @lcpr case=start
# 2147483647\n
# @lcpr case=end

#

