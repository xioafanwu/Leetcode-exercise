#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:return l2
        if not l2:return l1
        res = []
        while l1:
            res.append(l1.val)
            l1 = l1.next
        while l2:
            res.append(l2.val)
            l2 = l2.next
        res.sort()
        head = ListNode(res[0])
        cur = head
        for i in range(1,len(res)):
            newNode = ListNode(res[i])
            cur.next = newNode
            cur = newNode
        return head
# @lc code=end

