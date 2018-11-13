# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        v = ListNode(0)
        v.next = head
        p = v
        while p.next != None:
            q = p
            flag = False
            while q.next.next != None and q.next.val == q.next.next.val:
                q = q.next
                flag = True
            if flag:
                p.next = q.next.next
            else:
                p = p.next
        return v.next