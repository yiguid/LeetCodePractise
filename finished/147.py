# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        v = ListNode(0)
        v.next = head
        k = head.next #processing number
        preK = head
        while k != None:
            pre = v
            p = v.next
            while p != k:
                if p.val <= k.val:
                    pre = p
                    p = p.next
                else:
                    pre.next = k
                    preK.next = k.next
                    k.next = p
                    k = preK
                    p = k
            preK = k
            k = k.next
        return v.next

        
    def printList(self,head):
        p = head
        while p != None:
            print(p.val)
            p = p.next


s = Solution()

head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(0)
head.next.next.next = ListNode(3)

newHead = s.insertionSortList(head)
s.printList(newHead)
