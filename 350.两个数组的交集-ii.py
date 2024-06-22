#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nu1_table = {}
        nu2_table = {}
        for num in nums1:
            nu1_table[num] = nu1_table.get(num, 0) + 1
        for num in nums2:
            nu2_table[num] = nu2_table.get(num,0) + 1
        res = []
        for k,v in nu1_table.items():
            if k in nu2_table:
                res += [k] * min(v,nu2_table[k])
        return res
# @lc code=end

