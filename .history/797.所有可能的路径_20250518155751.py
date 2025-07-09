#
# @lc app=leetcode.cn id=797 lang=python3
# @lcpr version=30201
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def graph(graph,x,n,path,result):
            if x==n:
                result.append(path.copy())
                return
            for i in range(n):
                if graph[]
            
        dfs(graph)
# @lc code=end



#
# @lcpr case=start
# [[1,2],[3],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,1],[3,2,4],[3],[4],[]]\n
# @lcpr case=end

#

