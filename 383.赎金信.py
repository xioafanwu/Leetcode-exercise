#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #依次寻找，找到了建议，看能不能找到
        r_dict={}
        for i in magazine:
            r_dict[i]=r_dict.get(i,0)+1
        count=0
        for i in ransomNote:
            if i in r_dict:
                if r_dict[i]!=0:
                    count+=1
                r_dict[i]-=1
        if count==len(ransomNote):
            return True
        else:
            return False
# @lc code=end

