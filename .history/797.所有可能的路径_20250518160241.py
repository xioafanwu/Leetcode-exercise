#
# @lc app=leetcode.cn id=797 lang=python3
# @lcpr version=30201
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = list()
        stk = list()

        def dfs(x: int):
            if x == len(graph) - 1:
                ans.append(stk[:])
                return
            
            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()
        
        stk.append(0)
        dfs(0)
        return ans

# @lc code=end



#
# @lcpr case=start
# [[1,2],[3],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,1],[3,2,4],[3],[4],[]]\n
# @lcpr case=end

#

