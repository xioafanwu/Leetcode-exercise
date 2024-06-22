#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[p]=nums[i]
                p+=1
        return p
# @lc code=end

