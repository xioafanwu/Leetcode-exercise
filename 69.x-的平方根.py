#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,x
        while left<=right:
            mid=(left+right)//2
            if mid**2==x:
                return mid
            elif (mid**2<x)&((mid+1)**2>x):
                return mid
            elif mid**2<x:
                left=mid+1
            elif mid**2>x:
                right=mid-1

# @lc code=end

