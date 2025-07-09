#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30201
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def panduan(L,R):
            if not L and not R:
                return False
            if not L or not R or L.val!=R.val:
                return False
            return panduan(L.left,R.right) and panduan(L.right,R.left)
        return not root or panduan(root.left,root.right)

# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

