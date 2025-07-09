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
        def panduan(root.left,root.right):
            if not root.left and not root.right:
                return False
            if not root.left or not root.right or root.left.val!=root.right.val:
                return False
            return panduan(root.left.left,root.right.right) and panduan(root.left.right,root.right.left)
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

