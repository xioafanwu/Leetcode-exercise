#
# @lc app=leetcode.cn id=695 lang=python3
# @lcpr version=30201
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def dfs(self,grid,visited,x,y):
        global count
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        for i,j in direction:
            next_x=x+i
            next_y=y+j
            if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]=='1':
                visited[next_x][next_y]=True
                count+=1
                self.dfs(grid,visited,next_x,next_y)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        res=0
        visited=[[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and visited[i][j]==False:
                    count=1
                    res+=1
                    visited[i][j]=True
                    self.dfs(grid,visited,i,j)
        if res>0:
            return count
        else:
            return 0
# @lc code=end

#
# @lcpr case=start
# \n[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,0,0,0,0,0]]\n
# @lcpr case=end

#

