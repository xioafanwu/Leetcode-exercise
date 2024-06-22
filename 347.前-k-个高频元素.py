#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        result=[]
        for i in nums:
            dict[i]=dict.get(i,0)+1
        sorted_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
        for i in range(len(sorted_dict)):
            if i<k:
                result.append(sorted_dict[i][0])
        return result

# @lc code=end

