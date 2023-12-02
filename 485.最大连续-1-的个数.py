#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        cont=0
        for i in range(len(nums)):
            if nums[i] == 1:
                cont=cont+1
            else:
                ans=max(ans,cont)
                cont=0
        return max(ans,cont)
# @lc code=end

