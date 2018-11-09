# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        preHead = newHead
        i = m
        while i > 1:
            preHead = head
            head = head.next
            i -= 1
        times = n - m + 1
        pre = None
        cur = head
        while times > 0:
            #begin
            nextN = cur.next
            cur.next = pre
            pre = cur
            cur = nextN
            times -= 1
        preHead.next = pre
        head.next = cur
        return newHead.next




s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

newHead = s.reverseBetween(head, 2, 3)
while newHead != None:
    print(newHead.val)
    newHead = newHead.next
