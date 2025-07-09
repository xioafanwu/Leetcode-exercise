#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30201
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return self.result
        self.breaktracking(digits,0)
        return self.result
    def breaktracking(self,digits,index):
        if index == len(digits):
            self.result.append(self.s)
            return
        digit=int(digits[index])
        letters=self.letterMap[digit]
        for i in range(len(letters)):
            self.s+=letters[i]
            self.breaktracking(digits,index+1)
            self.s=self.s[:-1]
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

