class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ptr = ListNode()
        if l1 == None and l2 == None:
            return head.next
        
        carry = 0
        while l1 != None and l2 != None:
            _sum = l1.val + l2.val + carry
            ptr.next = ListNode(val = _sum % 10)
            if _sum >= 10:
                carry = 1
            else:
                carry = 0
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 == None:
            while l2 != None:
                _sum = l2.val + carry
                ptr.next = ListNode(val = _sum % 10)
                if _sum >= 10:
                    carry = 1
                else:
                    carry = 0
                ptr = ptr.next
                l2 = l2.next
                
        if l2 == None:
            while l1 != None:
                _sum = l1.val + carry
                ptr.next = ListNode(val = _sum % 10)
                if _sum >= 10:
                    carry = 1
                else:
                    carry = 0
                ptr = ptr.next
                l1 = l1.next
        
        if carry == 1:
            ptr.next = ListNode(val = 1)
        
        return head.next
                
