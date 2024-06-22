#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return 0
        map='0123456789abcdef'
        result=''
        if num<0:
            num=2**32+num
        while num<0:
            digit=num%16
            num=(num-digit)//16
            result
# @lc code=end

