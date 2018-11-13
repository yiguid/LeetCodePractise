# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lHead, lTail, rHead, rTail = None, None, None, None
        while head:
            if head.val < x:
                if lHead == None:
                    lHead = head
                    lTail = head
                else:
                    lTail.next = head
                    lTail = lTail.next
            else:
                if rHead == None:
                    rHead = head
                    rTail = head
                else:
                    rTail.next = head
                    rTail = rTail.next
            head = head.next

        if lHead != None:
            lTail.next = rHead
        else:
            lHead = rHead
        if rHead != None:
            rTail.next = None

        return lHead

    def partition2(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # empty head node mechanism
        head1 = curr1 = ListNode(0)
        head2 = curr2 = ListNode(0)
        curr = head
        while curr:
            if curr.val < x:
                curr1.next = curr
                curr1 = curr1.next
            else:
                curr2.next = curr
                curr2 = curr2.next
            curr = curr.next
        curr1.next = head2.next
        curr2.next = None
        return head1.next


s = Solution()

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

print(s.partition(head, 3).next.val == 2)