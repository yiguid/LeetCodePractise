# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        #split
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next
        #reverse [slow, end]
        pre = None
        cur = slow
        while cur != None:
            cur.next, pre, cur = pre, cur, cur.next
        #pre is the right part head
        l, r = head, pre
        while r != None:
            tmp = r.next
            r.next = l.next
            l.next = r
            l = r.next
            r = tmp
        l.next = None

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

s.reorderList(head)
s.printList(head)