# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            #be careful of the order
            slow.next, rev, slow = rev, slow, slow.next
        #if odd
        if fast != None:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
