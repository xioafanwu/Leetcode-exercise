#
# @lc app=leetcode.cn id=557 lang=python3
# @lcpr version=30201
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        result=[]
        for i in s_list:
            i_new=[i[j] for j in range(len(i),-1,-1)]
            result.append(''.join(i_new))
        return ' '.join(result)
# @lc code=end



#
# @lcpr case=start
# "Let's take LeetCode contest"\n
# @lcpr case=end

# @lcpr case=start
# "Mr Ding"\n
# @lcpr case=end

#

