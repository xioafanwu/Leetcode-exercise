#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30104
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if n>1:
            result=[[1],[1,1]]
            for i in range(2,numRows):
                dp=[1]*(i+1)
                for j in range(1,i):
                    dp[j]=result[i-1][j]+result[i-1][j-1]
                result.append(dp)
        return result
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

