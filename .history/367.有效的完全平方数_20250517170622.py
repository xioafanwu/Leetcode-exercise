#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=0,num
        while left<=right:
            mid=(left+right)//2
            if mid**2==num:
                return True
            if mid**2<num:
                left=mid+1
            if mid**2>num:
                right=mid-1
        return False
# @lc code=end

