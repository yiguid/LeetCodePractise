# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     v = ListNode(0)
    #     p = v
    #     while l1 != None or l2 != None:
    #         if l1 == None and l2 != None:
    #             p.next = l2
    #             l2 = l2.next
    #         elif l1 != None and l2 == None:
    #             p.next = l1
    #             l1 = l1.next
    #         else:
    #             if l1.val <= l2.val:
    #                 p.next = l1
    #                 l1 = l1.next
    #             else:
    #                 p.next = l2
    #                 l2 = l2.next
    #         p = p.next
    #     return v.next

    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     l = len(lists)
    #     if l <= 0:
    #         return None
    #     elif l == 1:
    #         return lists[0]
    #     else:
    #         left = lists[0]
    #         for i in range(1, l):
    #             left = self.mergeTwoLists(left, lists[i])
    #         return left

    #use heap
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop
        node_pools = []
        lookup = collections.defaultdict(list)
        for head in lists:
            if head:
                heappush(node_pools, head.val)
                lookup[head.val].append(head)
        dummy = cur = ListNode(None)
        while node_pools:
            smallest_val = heappop(node_pools)
            smallest_node = lookup[smallest_val].pop(0)
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heappush(node_pools, smallest_node.next.val)
                lookup[smallest_node.next.val].append(smallest_node.next)
        return dummy.next
