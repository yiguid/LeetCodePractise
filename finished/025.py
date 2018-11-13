# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2 or head == None:
            return head
        l = r = head
        newHead = None
        v = head
        while True:
            i = 0
            # [l,r) needs reverse
            while i < k and r != None:
                r = r.next
                i += 1 
            if i == k:
                #todo
                p = r
                q = l
                while q != r:
                    q.next, p, q = p, q, q.next
                if newHead == None:
                    newHead = p
                else:
                    v.next = p
                    v = l
                l = r
            else:
                if newHead == None:
                    return head
                else:
                    return newHead
    def printList(self,head):
        p = head
        while p != None:
            print(p.val)
            p = p.next


s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

newHead = s.reverseKGroup(head, 2)
s.printList(newHead)
        