#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30201
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        n=len(grid)
        m=len(grid[0])
        visited=[[False]*m for i in range(n)]
        res=0
        for i in range(len(grid)):
            for j in range(m):
                if grid[i][j]==1 and not visited[i][j]:
                    res+=1
                    visited[i][j]=True
                    dfs[grid,visited,i,j]
        return res
    def dfs(grid,visited,x,y):
        for i,j in direction:
            next_x=x+i
            next_y=y+j
            if next_x<0 or next_x>len(grid[0]) or next_y<0 or next_y>len(grid):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                dfs(grid,visited,next_x,next_y)
# @lc code=end



#
# @lcpr case=start
# [\n["1","1","1","1","0"],\n["1","1","0","1","0"],\n["1","1","0","0","0"],\n["0","0","0","0","0"]\n]\n
# @lcpr case=end

# @lcpr case=start
# [\n["1","1","0","0","0"],\n["1","1","0","0","0"],\n["0","0","1","0","0"],\n["0","0","0","1","1"]\n]\n
# @lcpr case=end

#

