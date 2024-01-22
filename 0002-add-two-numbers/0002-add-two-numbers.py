# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        res = temp
        c = 0
        while l1 or l2:
            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0
            s = p1 + p2 + c
            c = s // 10
            temp.next = ListNode(s - 10 if s >= 10 else s)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if c > 0:
            temp.next = ListNode(c)
        return res.next