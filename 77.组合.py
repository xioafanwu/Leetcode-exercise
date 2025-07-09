#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30201
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.breaktracking(n,k,1,[],result)
        return result
    def breaktracking(self,n,k,startindex,path,result):
        if len(path)==k:
            result.append(path[:])
            return
        for i in range(startindex,n+1):
            path.append(i)
            self.breaktracking(n,k,i+1,path,result)
            path.pop()
        
# @lc code=end



#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

