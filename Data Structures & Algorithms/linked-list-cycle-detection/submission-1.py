class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c = head
        visited = set()
        while c:
            visited.add(c)
            c = c.next
            if c!=None and c in visited:
                return True
        
        return False

            

        