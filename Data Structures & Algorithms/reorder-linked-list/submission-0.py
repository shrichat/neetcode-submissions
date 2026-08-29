# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next

        #reversing the second half
        slow.next = p = None
        c = second_half
        
        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt
        
        #merging both sides together
        c1 = head
        c2 = p

        while c1 and c2:
            nxt1 = c1.next
            nxt2 = c2.next

            c1.next = c2
            c2.next = nxt1
            
            c1 = nxt1
            c2 = nxt2

        

            

        