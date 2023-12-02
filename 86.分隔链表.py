#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=ListNode(-1)
        dummy2=ListNode(-1)
        p1,p2=dummy1,dummy2
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
            else:
                p2.next=head
                p2=p2.next
            temp=head.next
            head.next=None
            head=temp
        p1.next=dummy2.next
        return dummy1.next
# @lc code=end

