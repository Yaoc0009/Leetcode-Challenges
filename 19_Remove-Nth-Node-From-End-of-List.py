class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        
        if fast == None:
            head = head.next
            return head
    
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
