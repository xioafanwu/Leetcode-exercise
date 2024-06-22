#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getlength(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length
        lenA=getlength(headA)
        lenB=getlength(headB)
        p1,p2=headA,headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                p1=p1.next
        else:
            for i in range(lenB-lenA):
                p2=p2.next
        while p1!=p2:
            p1=p1.next
            p2=p2.next
        return p2
# @lc code=end

