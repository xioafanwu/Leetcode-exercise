#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a_dict={}
        for i in nums:
            a_dict[i]=a_dict.get(i,0)+1
        ans=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    var=target-nums[i]-nums[j]-nums[k]
                    if var in a_dict:
                        count=(nums[i]==var)+(nums[j]==var)+(nums[k]==var)
                        if count<a_dict[var]:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], var])))
        return [list(x) for x in ans]
# @lc code=end

