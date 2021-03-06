# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x)
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mid_node = self.find_middle_node(head)
        right_head = mid_node.next
        mid_node.next = None
        return self.merge(self.sortList(head), self.sortList(right_head))

    def find_middle_node(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head1, head2):
        """
        :type head1: ListNode
        :type head2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
        node.next = head1 or head2
        return dummy.next