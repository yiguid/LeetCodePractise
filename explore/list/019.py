# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        v = ListNode(0)
        v.next = head
        p = v
        q = head
        i = 1
        while i < n:
            q = q.next
            i += 1
        while q.next != None:
            p = p.next
            q = q.next
        p.next = p.next.next
        return v.next