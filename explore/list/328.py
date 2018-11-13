# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddHead = ListNode(0)
        oddCur = oddHead
        evenHead = ListNode(0)
        evenCur = evenHead
        counter = 1
        while head:
            if counter % 2 == 0:
                evenCur.next = head
                evenCur = evenCur.next
            else:
                oddCur.next = head
                oddCur = oddCur.next
            counter += 1
            head = head.next

        oddCur.next = evenHead.next
        evenCur.next = None
        return oddHead.next
        

s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print(s.oddEvenList(head).next.val == 3)