#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30104
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp[0]=[1]*(numRows+1)
        for i in range(1,numRows+1):
            for j in range(1,i+1):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        return dp
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

