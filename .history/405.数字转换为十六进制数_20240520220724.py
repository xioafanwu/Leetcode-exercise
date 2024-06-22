#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num>0:
            while t/16!=0:
                t=num
                num=0
                while t!=0:
                    t%16
# @lc code=end

