#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30201
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sb=[]
        for i in s:
            if i.isalnum():
                sb.append(i.lower())
        s=''.join(sb)
        left,right=0,len(n)-1
        while left<right:
            if s[left]=s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

