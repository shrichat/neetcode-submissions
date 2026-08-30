# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #finding middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next

        #reverse second half
        slow.next = p = None
        c = second_half
        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt

        #merge sides together alternatively
        tail = p
        start = head

        while start and tail:
            nxt1 = start.next
            nxt2 = tail.next

            start.next = tail
            tail.next = nxt1
            tail = nxt2
            start = nxt1
        


             

        
        