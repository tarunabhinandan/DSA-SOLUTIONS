# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        current = head
        frequency = 0
        while current is not None:
            frequency += 1
            current = current.next
        index = frequency - n
        if index == 0:
            head = head.next
            return head
        prev = None
        temp = head
        for i in range(index):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return head
        