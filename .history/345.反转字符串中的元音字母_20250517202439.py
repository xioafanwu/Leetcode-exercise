#
# @lc app=leetcode.cn id=345 lang=python3
# @lcpr version=30201
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right=0,len(s)-1
        s=list(s)
        s_dict={}
        f_dict={}
        j=0
        while left<right:
            if s[left] not in ['a','e','i','o','u','A','E','I','O','U']:
                left+=
            if s[right] not in['a','e','i','o','u','A','E','I','O','U']:
                right-=1
            if s[left] in ['a','e','i','o','u','A','E','I','O','U'] and s[right] in ['a','e','i','o','u','A','E','I','O','U']:
                temp=s[left]
                temp_r=s[right]
                s[left]=temp_r
                s[right]=temp
        s=''.join(s)
        return s
# @lc code=end



#
# @lcpr case=start
# "IceCreAm"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

#

