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
        if not list1:return list2
        if not list2:return list1
        res = []
        while list1:
            res.append(list1.val)
            list1 = list1.next
        while l2:
            res.append(list2.val)
            list2 = list2.next
        res.sort()
        head = ListNode(res[0])
        cur = head
        for i in range(1,len(res)):
            newNode = ListNode(res[i])
            cur.next = newNode
            cur = newNode
        return head
# @lc code=end

