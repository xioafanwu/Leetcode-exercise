#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':400,'CD':400,'CM':900}
        output=0
        T=True
        for i in range(len(s)):
            if T:
                if (i<len(s)-1):
                    if (dic[s[i]]>=dic[s[i+1]]):
                        output=dic[s[i]]+output
                    else:
                        output=output+dic[s[i+1]]-dic[s[i]]
                        T=False
                else:
                    if (dic[s[i]]<=dic[s[i-1]]):
                        output=dic[s[i]]+output
                    else:
                        output=output
            else:
                T=True
                continue
        return output
# @lc code=end