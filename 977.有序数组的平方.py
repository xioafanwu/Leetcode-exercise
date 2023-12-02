#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        i,j,pos=0,len(nums)-1,len(nums)-1
        while i<=j:
            if nums[i]**2>nums[j]**2:
                output[pos]=nums[i]**2
                i+=1
            else:
                output[pos]=nums[j]**2
                j-=1
            pos-=1
        return output
# @lc code=end

