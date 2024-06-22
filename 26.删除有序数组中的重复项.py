#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p,q=0,1
        while q<len(nums):
            if nums[p]==nums[q]:
                q=q+1
            else:
                nums[p+1]=nums[q]
                p=p+1
        return p+1
# @lc code=end

