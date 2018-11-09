# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
        	return l2
        if not l2:
        	return l1

        if l1.val + l2.val < 10:
        	l3 = ListNode(l1.val + l2.val)
        	l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
        	l3 = ListNode(l1.val + l2.val - 10)
        	tmp = ListNode(1)
        	l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, tmp))
        return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(l3.val, l3.next.val, l3.next.next.val)
