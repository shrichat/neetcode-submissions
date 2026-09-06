# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergetwo(list1, list2):
            dummy = ListNode()
            tail = dummy

            l1 = list1
            l2 = list2

            while l1 and l2:
                nxt1 = l1.next
                nxt2 = l2.next

                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = nxt1
                else:
                    tail.next = l2
                    l2 = nxt2
                
                tail = tail.next
            
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2
            
            return dummy.next
        
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]

                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                mergedLists.append(mergetwo(l1, l2))

            lists = mergedLists

        return lists[0]
            

            





        


        
            
            


        