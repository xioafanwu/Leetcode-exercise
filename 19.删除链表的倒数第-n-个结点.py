#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def listlength(head):
            length=0
            while head:
                length+=1
                head=head.next
            return length
        dummy=ListNode(0,head)
        cur=dummy
        length=listlength(head)
        for i in range(1,length-n+1):
            cur=cur.next
        cur.next = cur.next.next
        return dummy.next

# @lc code=end

