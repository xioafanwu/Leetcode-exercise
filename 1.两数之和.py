#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target) :
        dict={}
        for i in range(len(nums)):
            tar=target-nums[i]
            if tar in dict:
                if dict[tar]==i:
                    continue
                return [i,dict[tar]]
            dict[nums[i]]=i
# @lc code=end

