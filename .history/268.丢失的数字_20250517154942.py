#
# @lc app=leetcode.cn id=268 lang=python3
# @lcpr version=30104
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
            if i==len(nums)-1:
                return i+1
# @lc code=end



#
# @lcpr case=start
# [3,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [9,6,4,2,3,5,7,0,1]\n
# @lcpr case=end

#

