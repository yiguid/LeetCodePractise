# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, left, right):
        if left.val > right.val:
            left, right = right, left
        head = p = left
        left = left.next
        while left != None and right != None:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next

        if left != None:
            p.next = left
        else:
            p.next = right

        return head


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        res = self.merge(left, right)
        return res

        
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

newHead = s.sortList(head)
s.printList(newHead)
