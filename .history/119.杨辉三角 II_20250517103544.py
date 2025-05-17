#
# @lc app=leetcode.cn id=119 lang=python3
# @lcpr version=30104
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[[1],[1,1]]
        for i in range(2,rowIndex+1):
            dp=[1]*(i+1)
            for j in range(1,i-1):
                dp[j]=result[i-1][j-1]+result[i-1][j]
            result.append(dp)
        return result[rowIndex]
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

