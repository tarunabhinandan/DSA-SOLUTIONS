# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            head = slow.next
            return head
        current = fast
        while current.next is not None:
            current = current.next
            slow = slow.next
        slow.next = slow.next.next
        return head