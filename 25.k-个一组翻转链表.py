#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getlength(head):
            nums=0
            while head:
                nums+=1
                head=head.next
            return nums
        length=getlength(head)
        dummy=ListNode(-1,next=head)
        p0=dummy
        while length>=k:
            pre=None
            cur=p0.next
            for _ in range(k):
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
            nxt=p0.next
            p0.next.next=cur
            p0.next=pre
            p0=nxt
            length=length-k
        return dummy.next

# @lc code=end

