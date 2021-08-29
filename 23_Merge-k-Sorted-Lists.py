import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for ls in lists:
            while ls:
                heapq.heappush(h, ls.val)
                ls = ls.next
        
        ptr = head = ListNode()
        for _ in range(len(h)):
            ptr.next = ListNode(val=heapq.heappop(h))
            ptr = ptr.next
        return head.next
