class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = ls = ListNode()
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                ptr.next = ListNode(val=l1.val)
                l1 = l1.next
            else:
                ptr.next = ListNode(val=l2.val)
                l2 = l2.next
            ptr = ptr.next
        
        if l1 == None and l2 == None:
            return ls.next
        elif l1 == None:
            ptr.next = l2
        elif l2 == None:
            ptr.next = l1
        
        return ls.next
