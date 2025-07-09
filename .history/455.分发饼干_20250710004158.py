#
# @lc app=leetcode.cn id=455 lang=python3
# @lcpr version=30201
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m,n=len(g),len(s)
        i=j=count=0
        while i<m and j<n:
            while j<n and g[i]>s[j]:
                j=j+1
            if j<n:
                count+=1
            i+=1
            j+=1
        return count
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,2,3]\n
# @lcpr case=end

#

