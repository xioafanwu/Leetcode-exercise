#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<right:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            right-=1
            left+=1
# @lc code=end

