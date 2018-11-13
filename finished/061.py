# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        curr = head
        size = 1
        while (curr.next is not None ):
            curr = curr.next
            size = size + 1
             
        curr.next = head
             
        for i in range(size - (k % size)):
            curr = curr.next
        
        new_head = curr.next 
        curr.next = None
        
        return new_head

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        #p is the pre of new head
        p, q = head, head
        i = 0
        l = 1 #len of the list
        while i < k:
            if q.next != None:
                q = q.next
            else:
                q.next = head
                q = q.next
                k = k % l + l 
            i += 1
            l += 1
        while q.next != None and q.next != head:
            p = p.next
            q = q.next
        if q.next == None:
            q.next = head
        head = p.next
        p.next = None
        return head

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(s.rotateRight(head, 60000000).val)
