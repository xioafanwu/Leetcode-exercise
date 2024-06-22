#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        res=set()
        while n not in res:
            res.add(n)
            n=sum(int(i)**2 for i in str(n))
            if n == 1:
                return True
        return False
# @lc code=end

