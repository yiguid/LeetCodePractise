# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        v = ListNode(0)
        v.next = head

        p = v
        while p.next != None and p.next.next != None:
            n1 = p.next
            n2 = n1.next
            n = n2.next

            n2.next = n1
            n1.next = n
            p.next = n2

            p = n1

        return v.next