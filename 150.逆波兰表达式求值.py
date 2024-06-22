#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i!='+' and i!='-' and i!='*' and i!='/':
                stack.append(int(i))
            else:
                num2=stack.pop()
                num1=stack.pop()
                if i=='+':
                    stack.append(num1+num2)
                if i == '-':
                    stack.append(num1-num2)
                if i == '*':
                    stack.append(num2*num1)
                if i=='/':
                    stack.append(int(num1/num2))
        return stack[0]

# @lc code=end

