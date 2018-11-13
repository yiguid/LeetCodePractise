# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        v = ListNode(0)
        v.next = head
        p = v
        while p.next != None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return v.next