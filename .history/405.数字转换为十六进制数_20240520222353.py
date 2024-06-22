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
                i=0
                while t<16:
                    t=t//16
                    i=i+1
                    x=num-16**i
                    
# @lc code=end

