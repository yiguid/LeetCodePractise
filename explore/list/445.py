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
        s1, s2 = [], []
        p1, p2 = l1, l2
        while p1:
            s1.append(p1.val)
            p1 = p1.next
        while p2:
            s2.append(p2.val)
            p2 = p2.next
        t = 0
        head = None
        while s1 or s2 or t != 0:
            n = t
            if s1 != []:
                n += s1.pop()
            if s2 != []:
                n += s2.pop()
            node = ListNode(n % 10)
            t = n // 10
            node.next = head
            head = node
        return head
        

l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(l3.val, l3.next.val, l3.next.next.val, l3.next.next.next.val)