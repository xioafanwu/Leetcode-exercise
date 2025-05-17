#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30104
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        while left<=right:
            mid=(left+right)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                left=mid+1
            elif mid**2>x:
                right=mid-1
                return mid
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#

