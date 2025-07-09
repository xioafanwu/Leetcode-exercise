#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30201
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.backtracking(nums, [], [False] * len(nums), result)
        return result
    def backtracking(self,nums,path,used,result):
        if len(path)==len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i]=True
            path.append(nums[i])
            self.backtracking(nums,path,used,result)
            path.pop()
            used[i]=False
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

