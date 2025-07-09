#
# @lc app=leetcode.cn id=216 lang=python3
# @lcpr version=30201
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.breaktracking(n,k,1,[],result)
        return result
    def breaktracking(self,n,k,startindex,path,result):
        if sum(path)>n:
            return
        if (sum(path)==n) & len(path)==k:
            result.append(path[:])
            return
        for i in range(startindex,n+1):
            path.append(i)
            self.breaktracking(n,k,i+1,path,result)
            path.pop()
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n9\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n
# @lcpr case=end

#

