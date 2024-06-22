#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        records={}
        result={}
        coun=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                records[nums1[i]+nums2[j]]=records.get(nums1[i]+nums2[j],0)+1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                if -(nums3[i]+nums4[j]) in records:
                    coun+=records[-(nums3[i]+nums4[j])]
        return coun
# @lc code=end

