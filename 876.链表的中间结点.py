#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getlength(head):
            length=0
            while head:
                length+=1
                head=head.next
            return length
        length=getlength(head)
        if length//2==0:
            n=length/2
        else:
            n=length//2+1
        dummy=ListNode(0,head)
        cur=dummy
        for i in range(1,int(n)):
            cur=cur.next
        return cur.next
# @lc code=end

