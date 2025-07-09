#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30201
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if len(length)==0:
            return 0
        dp=[[0]*2 for _ in range(length)]
        for i in range(1,length):
            dp[i][0]=max(dp[i-1][0],-prices[i])
            dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0])
        return dp[-1][-1]
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

